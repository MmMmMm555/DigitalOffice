from rest_framework.serializers import ModelSerializer, ValidationError, CharField, ListField, StringRelatedField
from django.db import transaction
from datetime import date, timedelta

from apps.orders import models
from apps.users.models import User
from apps.mosque.models import Mosque
from apps.common.regions import Districts
from apps.orders.models import States
from apps.users.models import Role


class DirectionFilesSerializer(ModelSerializer):
    class Meta:
        model = models.DirectionFiles
        fields = ('id', 'file',)


class DirectionCreateSerializer(ModelSerializer):
    to_role = ListField(child=CharField())

    class Meta:
        model = models.Directions
        fields = (
            'id',
            'title',
            'creator',
            'file',
            'comments',
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
        extra_kwargs = {
            'creator': {'required': True},
            'from_role': {'required': True},
            'to_role': {'required': True},
            'from_date': {'required': True},
        }

    def validate(self, attrs):
        if int(attrs.get('from_role')) in attrs.get('to_role'):
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
                employee = User.objects.filter(role__in=to_role)
                print(to_role)
                print(employee)
                employee_list = direction.to_employee.all()
                district_list = direction.to_district.all()
                region_list = direction.to_region.all()
        # filtering m2m fields
                print(region_list)
                if not region_list:
                    models.DirectionsEmployeeRead.objects.bulk_create(
                        [
                            models.DirectionsEmployeeRead(
                                direction=direction, employee=i)
                            for i in employee
                        ]
                    )
                else:
                    if region_list:
                        employee = employee.filter(region__in=region_list)
                    if district_list:
                        employee = employee.filter(district__in=district_list)
                    if employee_list:
                        employee = employee.filter(
                            profil__mosque__id__in=employee_list)
                    print(employee)
                    employee_to_create = [
                        models.DirectionsEmployeeRead(
                            direction=direction, employee=i)
                        for i in employee
                    ]
                    print(employee_to_create)
                    models.DirectionsEmployeeRead.objects.bulk_create(
                        employee_to_create)

        # if employee_list:
        #             models.DirectionsEmployeeRead.objects.bulk_create(
        #                 [
        #                     models.DirectionsEmployeeRead(
        #                         direction=direction, employee=i)
        #                     for i in employee.filter(profil__mosque__id__in=employee_list)
        #                 ]
        #             )
        # elif district_list:
        #             employee = employee.filter(
        #                 district__in=district_list, region__in=region_list)
        #             employee_to_create = [
        #                 models.DirectionsEmployeeRead(
        #                     direction=direction, employee=i)
        #                 for i in employee
        #             ]
        #             models.DirectionsEmployeeRead.objects.bulk_create(
        #                 employee_to_create)
        # else:
        #             district_list = Districts.objects.filter(
        #                 region__in=region_list,)
        #             # creating direction_read models
        #             employee_to_create = [
        #                 models.DirectionsEmployeeRead(
        #                     direction=direction, employee=i)
        #                 for i in employee.filter(district__in=district_list)
        #             ]
        #             models.DirectionsEmployeeRead.objects.bulk_create(
        #                 employee_to_create)

        # getting m2m require field values
                employee_required = employee
                employee_list_required = direction.required_to_employee.all()
                district_list_required = direction.required_to_district.all()
                region_list_required = direction.required_to_region.all()

        #

        #         # filtering m2m required fields
                if employee_list_required:
                    models.DirectionsEmployeeRead.objects.filter(
                        direction=direction,
                        employee__in=employee_required.filter(
                            profil__mosque__id__in=employee_list_required)
                    ).update(requirement=True)
                elif district_list_required:
                    employee_required = employee_required.filter(
                        region__in=region_list_required, district__in=district_list_required)
                    models.DirectionsEmployeeRead.objects.filter(
                        direction=direction,
                        employee__in=employee_required
                    ).update(requirement=True)
                else:
                    district_list_required = Districts.objects.filter(
                        region__in=region_list_required)

                    # updating direction_read requirement
                    models.DirectionsEmployeeRead.objects.filter(
                        direction=direction,
                        employee__in=employee_required.filter(
                            district__in=district_list_required)
                    ).update(requirement=True)

        #         # setting m2m field values to direction
        #         direction.required_to_district.set(district_list_required)
        #         direction.required_to_region.set(region_list_required)
        #         direction.to_district.set(district_list)
        #         direction.to_region.set(region_list)

        #         # saving direction
                return direction
        except:
            raise ValidationError('Something went wrong')


class DirectionListSerializer(ModelSerializer):
    to_role = ListField(
        child=CharField(), read_only=True)
    from_region = StringRelatedField(read_only=True)
    from_district = StringRelatedField(read_only=True)

    class Meta:
        model = models.Directions
        fields = ('id',
                  'title',
                  'created_at',
                  'from_region',
                  'from_district',
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
    to_role = ListField(
        child=CharField(), read_only=True)
    file = DirectionFilesSerializer(many=True)

    class Meta:
        model = models.Directions
        fields = ('id',
                  'title',
                  'creator',
                  'direction_type',
                  'file',
                  'comments',
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
        representation['creator'] = User.objects.filter(
            id=instance.creator.id).values('id', 'profil__name', 'profil__last_name',)
        if instance.to_employee:
            representation['to_employee'] = instance.to_employee.all().values(
                'id', 'name', 'district__name', 'region__name',)
        if instance.required_to_employee:
            representation['required_to_employee'] = instance.required_to_employee.all(
            ).values('id', 'name', 'district__name', 'region__name',)
        seen = models.DirectionsEmployeeRead.objects.filter(direction=instance)
        representation['waiting'] = seen.filter(state=States.UNSEEN).count()
        representation['accepted'] = seen.filter(state=States.ACCEPTED).count()
        representation['done'] = seen.filter(state=States.DONE).count()
        return representation


class DirectionUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Directions
        fields = (
            'id',
            'title',
            'file',
            'comments',
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
            'from_date': {'required': False},
        }

    def validate(self, attrs):
        if self.instance.direction_employee_result.all():
            raise ValidationError('you can not edit now')
        else:
            models.DirectionsEmployeeRead.objects.filter(
                direction=self.instance).update(state=States.UNSEEN)
        return attrs

    # def save(self):
    #     obj = models.Directions.objects.filter(
    #         id=self.instance.id).update(**self.validated_data)
    #     models.DirectionsEmployeeRead.objects.filter(
    #         direction=self.instance).update(state=States.UNSEEN)
    #     return obj
