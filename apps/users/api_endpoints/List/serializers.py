from rest_framework import serializers

from apps.users.models import User


class UsersListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='profil.name', read_only=True)
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


class UsersDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'role',
                  'email', 'profil', 'region', 'district',)
        depth = 1


class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'role',
                  'email', 'profil', 'region', 'district',)
        extra_kwargs = {
            'username': {'required': False},
        }