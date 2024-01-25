from rest_framework.serializers import ModelSerializer, CharField

from apps.employee import models
from apps.mosque.models import Mosque
from apps.orders.models import Directions
from apps.friday_tesis.models import FridayThesis
from apps.users.models import User


class DepartmentRelatedSerializer(ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('id', 'name',)
        read_only_fields = fields


class Graduated_UniverRelatedSerializer(ModelSerializer):
    class Meta:
        model = models.Graduation
        fields = ('id', 'name',)
        read_only_fields = fields


class PositionRelatedSerializer(ModelSerializer):
    class Meta:
        model = models.Position
        fields = ('id', 'name', 'department',)
        read_only_fields = fields


class FridayThesisRelatedSerializer(ModelSerializer):
    class Meta:
        model = FridayThesis
        fields = ('id', 'title', 'types', 'date',)
        read_only_fields = fields


class DirectionsRelatedSerializer(ModelSerializer):
    class Meta:
        model = Directions
        fields = ('id', 'title', 'direction_type', 'types',
                  'from_date', 'to_date', 'from_role',)
        read_only_fields = fields


class MosqueRelatedSerializer(ModelSerializer):
    region = CharField(source='region.name', default=None,)
    district = CharField(source='district.name', default=None,)

    class Meta:
        model = Mosque
        fields = ('id', 'name', 'address', 'region', 'district',)
        read_only_fields = fields


class EmployeeRelatedSerializer(ModelSerializer):
    user_role = CharField(source='profile.role', default=None) 
    class Meta:
        model = models.Employee
        fields = ('id', 'first_name', 'last_name', 'user_role',)
        read_only_fields = fields


class UserRelatedSerializer(ModelSerializer):
    first_name = CharField(source='profil.first_name', default=None)
    last_name = CharField(source='profil.last_name', default=None)

    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'profil',
                  'first_name', 'last_name',)
        read_only_fields = fields
