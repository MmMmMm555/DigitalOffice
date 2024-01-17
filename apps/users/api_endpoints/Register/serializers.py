from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.db.models import Q, Count

from apps.users.models import User, Role
from apps.mosque.models import Mosque


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'role',
            'region',
            'district',
            'profil',
            'password',
            'password2',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        # if attrs.get('role') == Role.IMAM and Mosque.objects.filter(employee=attrs.get('profil')).aggregate(has_imam=Count('employee', filter=Q(employee__profile__role=Role.IMAM))) != 0:
        #     raise serializers.ValidationError(
        #         {"detail": "You can not choose role 'imam' for this profile"})
        return attrs

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            role=validated_data.get('role'),
            region=validated_data.get('region'),
            district=validated_data.get('district'),
            profil=validated_data.get('profil'),
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user
