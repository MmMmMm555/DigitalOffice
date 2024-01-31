from rest_framework.serializers import ModelSerializer, ValidationError, CharField, ListField, StringRelatedField
from django.db import transaction

from apps.orders import models
from apps.users.models import User
from apps.common.regions import Districts
from apps.orders.models import States
from apps.common.api_endpoints.districts.serializers import RegionsSerializer
from apps.common.api_endpoints.regions.serializers import DistrictsSerializer
from apps.common.related_serializers import UserRelatedSerializer, MosqueRelatedSerializer
from apps.orders.tasks import create_direction_notifications


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
        with transaction.atomic():
            # creation instance
            direction = super().create(validated_data)
            create_direction_notifications.delay(direction.id)
            # direction = models.Directions.objects.get(id=direction.id)
            # # getting instance role
            # to_role = direction.to_role
            # # getting m2m field values
            # employee = User.objects.filter(role__in=to_role)
            # employee_list = direction.to_employee.all()
            # district_list = direction.to_district.all()
            # region_list = direction.to_region.all()
            # # filtering m2m fields
            # if not region_list:
            #     models.DirectionsEmployeeRead.objects.bulk_create(
            #         [
            #             models.DirectionsEmployeeRead(
            #                 direction=direction, employee=i)
            #             for i in employee
            #         ]
            #     )
            # else:
            #     if region_list:
            #         employee = employee.filter(region__in=region_list)
            #     if district_list:
            #         employee = employee.filter(district__in=district_list)
            #     if employee_list:
            #         employee = employee.filter(
            #             profil__mosque__id__in=employee_list)
            #     employee_to_create = [
            #         models.DirectionsEmployeeRead(
            #             direction=direction, employee=i)
            #         for i in employee
            #     ]
            #     models.DirectionsEmployeeRead.objects.bulk_create(
            #         employee_to_create)

            # # getting m2m require field values
            # employee_required = employee
            # employee_list_required = direction.required_to_employee.all()
            # district_list_required = direction.required_to_district.all()
            # region_list_required = direction.required_to_region.all()

            # # filtering m2m required fields
            # if employee_list_required:
            #     models.DirectionsEmployeeRead.objects.filter(
            #         direction=direction,
            #         employee__in=employee_required.filter(
            #             profil__mosque__id__in=employee_list_required)
            #     ).update(requirement=True)
            # elif district_list_required:
            #     employee_required = employee_required.filter(
            #         region__in=region_list_required, district__in=district_list_required)
            #     models.DirectionsEmployeeRead.objects.filter(
            #         direction=direction,
            #         employee__in=employee_required
            #     ).update(requirement=True)
            # else:
            #     district_list_required = Districts.objects.filter(
            #         region__in=region_list_required)
            #     models.DirectionsEmployeeRead.objects.filter(
            #         direction=direction,
            #         employee__in=employee_required.filter(
            #             district__in=district_list_required)
            #     ).update(requirement=True)
            return direction


class DirectionListSerializer(ModelSerializer):
    to_role = ListField(child=CharField(), read_only=True)
    from_region = CharField(source='creator.region.name', default=None)
    from_district = CharField(source='creator.district.name', default=None)
    to_district = DistrictsSerializer(many=True, read_only=True)
    to_region = RegionsSerializer(many=True, read_only=True)
    required_to_district = DistrictsSerializer(many=True, read_only=True)
    required_to_region = RegionsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Directions
        fields = ('id',
                  'title',
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
                  'to_date',
                  'created_at',
                  )
        read_only_fields = fields


class DirectionSingleSerializer(ModelSerializer):
    to_role = ListField(child=CharField(), read_only=True)
    file = DirectionFilesSerializer(many=True, read_only=True)
    creator = UserRelatedSerializer(many=False, read_only=True)
    to_district = DistrictsSerializer(many=True, read_only=True)
    to_region = RegionsSerializer(many=True, read_only=True)
    to_employee = MosqueRelatedSerializer(many=True, read_only=True)
    required_to_district = DistrictsSerializer(many=True, read_only=True)
    required_to_region = RegionsSerializer(many=True, read_only=True)
    required_to_employee = MosqueRelatedSerializer(many=True, read_only=True)

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
        read_only_fields = fields


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
