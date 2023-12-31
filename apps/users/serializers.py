
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        # token['email'] = user.email
        # token['role'] = user.role
        return token


