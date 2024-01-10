from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.users.api_endpoints.List.serializers import UsersListSerializer, UsersDetailSerializer
from apps.users.models import User
from apps.common.permissions import IsSuperAdmin


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer
    permission_classes = (IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ('id', 'role', 'region', 'district', 'profil__mosque',)
    search_fields = ('email', 'profil__name', 'profil__surname', 'username',)


class UsersDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersDetailSerializer
    permission_classes = (IsSuperAdmin,)