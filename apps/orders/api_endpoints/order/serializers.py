from rest_framework.serializers import ModelSerializer, ValidationError
from apps.orders import models
from apps.users.models import User
from apps.common.regions import Regions, Districts


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
            employee_list_required  = direction.required_to_employee.all()
            district_list_required  = direction.required_to_district.all()
            region_list_required  = direction.required_to_region.all()

            # filtering m2m fields
            employee = employee.filter(region__in=region_list)
            if employee_list:
                employee = employee.filter(id__in=employee_list.values_list('id', flat=True))
            elif district_list:
                employee = employee.filter(district__in=district_list)
            else:
                district_list = Districts.objects.filter(region__in=region_list)

            # filtering m2m required fields
            employee_required = employee_required.filter(region__in=region_list_required)
            if employee_list_required:
                employee_required = employee_required.filter(id__in=employee_list_required.values_list('id', flat=True))
            elif district_list_required:
                employee_required = employee_required.filter(district__in=district_list_required)
            else:
                district_list_required = Districts.objects.filter(region__in=region_list_required)
            # creating direction_read models
            for i in employee:
                models.DirectionsEmployeeRead.objects.create(
                        direction = direction,
                        employee = i,)
            # updating direction_read requirement
            models.DirectionsEmployeeRead.objects.filter(direction=direction, employee__in=employee_required).update(requirement=True)
            # setting m2m field values to direction
            direction.required_to_district.set(district_list_required)
            direction.to_district.set(district_list)
            direction.required_to_employee.set(employee_required)
            direction.to_employee.set(employee)
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
                  'to_date', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['seen_count'] = models.DirectionsEmployeeRead.objects.filter(direction=instance, state='2').count()
        representation['unseen_count'] = models.DirectionsEmployeeRead.objects.filter(direction=instance, state='1').count()
        return representation