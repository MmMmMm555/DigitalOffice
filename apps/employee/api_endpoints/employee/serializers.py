from rest_framework.serializers import ModelSerializer
from apps.employee import models


class WorkActivitySerializer(ModelSerializer):
    class Meta:
        model = models.WorkActivity
        fields = ('id', 'employee', 'start_date', 'end_date', 'company', 'as_who',)

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = models.SocialMedia
        fields = ('id', 'employee', 'social_media', 'link',)

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ('id', 'employee', 'type', 'activity', 'image',)

class EmployeeSerializer(ModelSerializer):
    class Meta:
       model = models.Employee
       depth = 1
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
                 'workactivity',
                 'activity',
                 'socialmedia',)

class EmployeeListSerializer(EmployeeSerializer):
    
    workactivity = WorkActivitySerializer
    socialmedia = SocialMediaSerializer
    activity = ActivitySerializer