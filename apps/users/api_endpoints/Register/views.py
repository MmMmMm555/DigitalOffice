from rest_framework import generics, parsers

from apps.users.api_endpoints.Register.serializers import RegisterSerializer
from apps.users.models import User
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsSuperAdmin

class RegisterView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsSuperAdmin)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer