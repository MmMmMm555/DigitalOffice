from rest_framework import generics

from apps.users.api_endpoints.Register.serializers import RegisterSerializer
from apps.users.models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
