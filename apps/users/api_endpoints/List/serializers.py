from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from apps.users.models import User
from apps.employee.models import Employee


class UsersListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='profil.first_name', read_only=True)
    last_name = serializers.CharField(
        source='profil.last_name', read_only=True)
    region_name = serializers.CharField(
        source='region.name', read_only=True)
    district_name = serializers.CharField(
        source='district.name', read_only=True)
    mosque = serializers.CharField(source='profil.mosque.name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'last_name', 'role',
                  'email', 'profil', 'region', 'region_name', 'district', 'district_name', 'mosque',)
        read_only_fields = fields


class UsersDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'role',
                  'email', 'profil', 'region', 'district',)
        depth = 1
        read_only_fields = fields


class UsersUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=False, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'role',
                  'email', 'profil', 'region', 'district', 'password',)
        extra_kwargs = {
            'username': {'required': False},
            'password': {'required': False},
        }

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()
        return super().update(instance, validated_data)


class SelfProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'phone_number',
                  'address',
                  'image',
                  'birth_date',
                  )
        extra_kwargs = {
            'first_name': {'required': False},
            'middle_name': {'required': False},
            'last_name': {'required': False},
            'phone_number': {'required': False},
            'address': {'required': False},
            'birth_date': {'required': False},
        }
