from rest_framework.serializers import ModelSerializer

from apps.employee import models
from apps.common.related_serializers import (
    MosqueRelatedSerializer, PositionRelatedSerializer, Graduated_UniverRelatedSerializer)


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = models.SocialMedia
        fields = ('id', 'employee', 'social_media', 'link',)


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'phone_number',
                  'address',
                  'image',
                  'gender',
                  'position',
                  'nation',
                  'birth_date',
                  'education',
                  'graduated_univer',
                  'graduated_year',
                  'diploma_number',
                  'academic_degree',
                  'mosque',
                  'achievement',
                  )
        extra_kwargs = {
            "graduated_year": {"required": False},
        }


class EmployeeUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'phone_number',
                  'address',
                  'image',
                  'gender',
                  'position',
                  'nation',
                  'birth_date',
                  'education',
                  'graduated_univer',
                  'graduated_year',
                  'diploma_number',
                  'academic_degree',
                  'mosque',
                  'achievement',
                  )
        extra_kwargs = {
            "gender": {"required": False},
            "first_name": {"required": False},
            "middle_name": {"required": False},
            "last_name": {"required": False},
            "phone_number": {"required": False},
            "address": {"required": False},
            "birth_date": {"required": False},
            "mosque": {"required": False},
            "graduated_year": {"required": False},
        }


class EmployeeListSerializer(ModelSerializer):
    mosque = MosqueRelatedSerializer(many=False, read_only=True)
    graduated_univer = Graduated_UniverRelatedSerializer(
        many=False, read_only=True)
    position = PositionRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = models.Employee
        fields = ('id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'phone_number',
                  'position',
                  'education',
                  'graduated_univer',
                  'graduated_year',
                  'academic_degree',
                  'mosque',)
        read_only_fields = fields


class EmployeeDetailSerializer(ModelSerializer):
    socialmedia = SocialMediaSerializer(many=True)
    mosque = MosqueRelatedSerializer(many=False, read_only=True)
    position = PositionRelatedSerializer(many=False, read_only=True)
    graduated_univer = Graduated_UniverRelatedSerializer(
        many=False, read_only=True)

    class Meta:
        model = models.Employee
        fields = ('id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'phone_number',
                  'address',
                  'image',
                  'gender',
                  'position',
                  'nation',
                  'birth_date',
                  'education',
                  'graduated_univer',
                  'graduated_year',
                  'diploma_number',
                  'academic_degree',
                  'mosque',
                  'achievement',
                  'socialmedia',
                  )
        read_only_fields = fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['department'] = None
        if instance.position:
            representation['department'] = {
                'id': instance.position.department.id, 'name': instance.position.department.name, 'position': instance.position.name, }
        return representation
