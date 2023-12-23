from rest_framework.serializers import ModelSerializer, ValidationError
from django.db import transaction
from datetime import date, timedelta

from apps.orders import models
from apps.users.models import User
from apps.common.regions import Districts

# class DirectionSerializer(ModelSerializer):
#     class Meta:
#         model = models.Directions
#         fields = ('id',
#                   'title',
#                   'direction_type',
#                   'file',
#                   'type',
#                   'to_role',
#                   'to_region',
#                   'to_district',
#                   'to_imams',
#                   'from_date',
#                   'to_date',
#                   'created_at',
#                   'updated_at',
#                   'voice',
#                   'image',
#                   'video',
#                   'comment',
#                   'file_bool',
#                   )

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['seen_count'] = models.DirectionsEmployeeRead.objects.filter(direction=instance, seen=True).count()
#         representation['unseen_count'] = models.DirectionsEmployeeRead.objects.filter(direction=instance, seen=False).count()
#         return representation


class DirectionCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Directions
        fields = (
            'id',
            'title',
            'file',
            'types',
            'direction_type',
            'from_role',
            'to_role',
            'to_region',
            'to_district',
            'to_employee',
            'required_to_region',
            'required_to_district',
            'required_to_employee',
            'from_date',
            'to_date',
            'voice',
            'image',
            'video',
            'comment',
            'file_bool',
        )

    def validate(self, attrs):
        if int(attrs.get('from_role')) >= int(attrs.get('to_role')):
            raise ValidationError('selected roles are not right position')
        return attrs

    def create(self, validated_data):
        try:
            with transaction.atomic():
                # creation instance
                direction = super().create(validated_data)
                direction = models.Directions.objects.get(id=direction.id)
                # getting instance role
                to_role = direction.to_role
                # getting m2m field values
                employee = User.objects.filter(role=to_role[0])
                employee_list = direction.to_employee.all()
                district_list = direction.to_district.all()
                region_list = direction.to_region.all()
                # getting m2m require field values
                employee_required = User.objects.filter(role=to_role[0])
                employee_list_required = direction.required_to_employee.all()
                district_list_required = direction.required_to_district.all()
                region_list_required = direction.required_to_region.all()

                # filtering m2m fields
                if employee_list:
                    models.DirectionsEmployeeRead.objects.bulk_create(
                        [
                            models.DirectionsEmployeeRead(
                                direction=direction, employee=i)
                            for i in employee.filter(id__in=employee_list.values_list('id', flat=True))
                        ]
                    )
                elif district_list:
                    employee = employee.filter(
                        district__in=district_list, region__in=region_list)
                else:
                    district_list = Districts.objects.filter(
                        region__in=region_list)

                # filtering m2m required fields
                if employee_list_required:
                    models.DirectionsEmployeeRead.objects.filter(
                        direction=direction,
                        employee__in=employee_required.filter(
                            id__in=employee_list_required.values_list('id', flat=True))
                    ).update(requirement=True)
                elif district_list_required:
                    employee_required = employee_required.filter(
                        region__in=region_list_required, district__in=district_list_required)
                else:
                    district_list_required = Districts.objects.filter(
                        region__in=region_list_required)

                # creating direction_read models
                employee_to_create = [
                    models.DirectionsEmployeeRead(
                        direction=direction, employee=i)
                    for i in employee.filter(district__in=district_list)
                ]
                models.DirectionsEmployeeRead.objects.bulk_create(
                    employee_to_create)

                # updating direction_read requirement
                models.DirectionsEmployeeRead.objects.filter(
                    direction=direction,
                    employee__in=employee_required.filter(
                        district__in=district_list_required)
                ).update(requirement=True)

                # setting m2m field values to direction
                direction.required_to_district.set(district_list_required)
                direction.to_district.set(district_list)
                direction.required_to_employee.set(
                    models.DirectionsEmployeeRead.objects.filter(
                        direction=direction, requirement=True).values_list('employee__id', flat=True)
                )
                direction.to_employee.set(
                    models.DirectionsEmployeeRead.objects.filter(
                        direction=direction).values_list('employee__id', flat=True)
                )

                # saving direction
                direction.save()
                return direction
        except:
            raise ValidationError('Something went wrong')


class DirectionListSerializer(ModelSerializer):
    class Meta:
        model = models.Directions
        fields = ('id',
                  'title',
                  'created_at',
                  'to_region',
                  'to_district',
                  'required_to_region',
                  'required_to_district',
                  'to_role',
                  'from_role',
                  'types',
                  'direction_type',
                  'from_date',
                  'to_date',)
        depth = 1


class DirectionSingleSerializer(ModelSerializer):
    class Meta:
        model = models.Directions
        fields = ('id',
                  'title',
                  'direction_type',
                  'file',
                  'to_region',
                  'to_district',
                  'to_employee',
                  'required_to_region',
                  'required_to_district',
                  'required_to_employee',
                  'to_role',
                  'from_role',
                  'types',
                  'from_date',
                  'to_date',
                  'voice',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  'created_at',
                  'updated_at',)
        depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.to_employee:
            representation['to_employee'] = User.objects.filter(
                id__in=instance.to_employee.all()).values('id', 'profil__name', 'profil__last_name',)
        if instance.required_to_employee:
            representation['required_to_employee'] = User.objects.filter(
                id__in=instance.required_to_employee.all()).values('id', 'profil__name', 'profil__last_name',)
        representation['waiting'] = models.DirectionsEmployeeRead.objects.filter(
            direction=instance, state='1').count()
        representation['accepted'] = models.DirectionsEmployeeRead.objects.filter(
            direction=instance, state='2').count()
        representation['done'] = models.DirectionsEmployeeRead.objects.filter(
            direction=instance, state='3').count()
        return representation


class DirectionUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Directions
        fields = (
            'id',
            'title',
            'file',
            'types',
            'direction_type',
            'from_date',
            'to_date',
            'voice',
            'image',
            'video',
            'comment',
            'file_bool',
        )
        extra_kwargs = {
            'title': {'required': False},
            'file': {'required': False},
        }

    def save(self):
        if self.instance.to_date <= date.today():
            raise ValidationError('editable date passed')
        obj = models.Directions.objects.filter(
            id=self.instance.id).update(**self.validated_data)
        models.DirectionsEmployeeRead.objects.filter(
            direction=self.instance).update(state='1')
        return obj


#     def validate(self, attrs):
#         if int(attrs.get('from_role')) >= int(attrs.get('to_role')):
#             raise ValidationError('selected roles are not right position')
#         return attrs

#     def create(self, validated_data):
#         try:
#             # creation instance
#             direction = super().create(validated_data)
#             direction = models.Directions.objects.get(id=direction.id)
#             # getting instance role
#             to_role = direction.to_role
#             # getting m2m field values
#             employee = User.objects.filter(role=to_role[0])
#             employee_list = direction.to_employee.all()
#             district_list = direction.to_district.all()
#             region_list = direction.to_region.all()
#             # getting m2m require field values
#             employee_required = User.objects.filter(role=to_role[0])
#             employee_list_required  = direction.required_to_employee.all()
#             district_list_required  = direction.required_to_district.all()
#             region_list_required  = direction.required_to_region.all()

#             # filtering m2m fields
#             if employee_list:
#                 for i in employee.filter(id__in=employee_list.values_list('id', flat=True)):
#                     try:
#                         models.DirectionsEmployeeRead.objects.create(
#                             direction = direction,
#                             employee = i,)
#                     except:
#                         pass
#             elif district_list:
#                 employee = employee.filter(district__in=district_list, region__in=region_list)
#             else:
#                 district_list = Districts.objects.filter(region__in=region_list)

#             # filtering m2m required fields
#             if employee_list_required:
#                 models.DirectionsEmployeeRead.objects.filter(direction=direction, employee__in=employee_required.filter(id__in=employee_list_required.values_list('id', flat=True))).update(requirement=True)
#             elif district_list_required:
#                 employee_required = employee_required.filter(region__in=region_list_required, district__in=district_list_required)
#             else:
#                 district_list_required = Districts.objects.filter(region__in=region_list_required)

#             # creating direction_read models
#             for i in employee.filter(district__in=district_list):
#                 try:
#                     models.DirectionsEmployeeRead.objects.create(
#                             direction = direction,
#                             employee = i,)
#                 except:
#                     pass
#             # updating direction_read requirement

#             models.DirectionsEmployeeRead.objects.filter(direction=direction, employee__in=employee_required.filter(district__in=district_list_required)).update(requirement=True)
#             # setting m2m field values to direction
#             direction.required_to_district.set(district_list_required)
#             direction.to_district.set(district_list)
#             direction.required_to_employee.set(models.DirectionsEmployeeRead.objects.filter(direction=direction, requirement=True).values_list('employee__id', flat=True))
#             direction.to_employee.set(models.DirectionsEmployeeRead.objects.filter(direction=direction).values_list('employee__id', flat=True))
#             # saving direction
#             direction.save()
#             return direction
#         except:
#             raise ValidationError('Something went wrong')
