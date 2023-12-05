from rest_framework import generics

from apps.users.serializers import RegisterSerializer
from apps.users.models import User
from rest_framework.permissions import IsAuthenticated
from ...permissions import IsSuperAdmin

class RegisterView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsSuperAdmin)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
