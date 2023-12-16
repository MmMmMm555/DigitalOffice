from rest_framework.serializers import ModelSerializer, CharField

from apps.employee import models
from apps.mosque.models import Mosque


# class WorkActivitySerializer(ModelSerializer):
#     class Meta:
#         model = models.WorkActivity
#         fields = ('id', 'employee', 'start_date', 'end_date', 'company', 'as_who',)

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = models.SocialMedia
        fields = ('id', 'employee', 'social_media', 'link',)

# class ActivitySerializer(ModelSerializer):
#     class Meta:
#         model = models.Activity
#         fields = ('id', 'employee', 'type', 'activity', 'image',)

class EmployeeSerializer(ModelSerializer):
    class Meta:
       model = models.Employee
       fields = ('id', 
                 'name', 
                 'surname', 
                 'last_name', 
                 'phone_number', 
                 'address', 
                 'image', 
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
            "image": {"required": True},
            "graduated_year": {"required": False},
            }


class EmployeeUpdateSerializer(ModelSerializer):
    class Meta:
       model = models.Employee
       fields = ('id', 
                 'name', 
                 'surname', 
                 'last_name', 
                 'phone_number', 
                 'address', 
                 'image', 
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
            "image": {"required": False},
            "name": {"required": False},
            "surname": {"required": False},
            "last_name": {"required": False},
            "phone_number": {"required": False},
            "address": {"required": False},
            "birth_date": {"required": False},
            "mosque": {"required": False},
            "graduated_year": {"required": False},
            }


class EmployeeListSerializer(ModelSerializer): 
    socialmedia = SocialMediaSerializer(many=True)
    mosque_name = CharField(source='mosque.name', read_only=True)
    mosque_address = CharField(source='mosque.address', read_only=True)
    class Meta:
       model = models.Employee
       fields = ('id',
                 'name', 
                 'surname', 
                 'last_name', 
                 'phone_number', 
                 'address', 
                 'image', 
                 'birth_date', 
                 'education',
                 'graduated_univer',
                 'graduated_year',
                 'diploma_number',
                 'academic_degree',
                 'mosque',
                 'mosque_name',
                 'mosque_address',
                 'achievement',
                 'socialmedia',)
