from rest_framework.serializers import ModelSerializer, CharField

from apps.employee import models
from apps.users import models


class EmployeeRelatedSerializer(ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id', 'name', 'last_name',)
        read_only_fields = fields


class UserRelatedSerializer(ModelSerializer):
    name = CharField(source='profil.name')
    last_name = CharField(source='profil.last_name')
    class Meta:
        model = models.User
        fields = ('id', 'username', 'role', 'profil', 'name', 'last_name',)
        read_only_fields = fields

