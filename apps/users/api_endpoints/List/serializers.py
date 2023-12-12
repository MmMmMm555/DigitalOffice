from rest_framework import serializers

from apps.users.models import User


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'profil', 'region', 'district',)
        depth = 1