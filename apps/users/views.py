from django.shortcuts import render
from apps.users.serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .permissions import IsSuperAdmin

from apps.users.serializers import RegisterSerializer
from apps.users.models import User

# Create your views here.


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsSuperAdmin)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
