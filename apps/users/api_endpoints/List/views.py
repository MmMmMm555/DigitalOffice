from rest_framework import generics, filters, parsers
from django_filters.rest_framework import DjangoFilterBackend

from apps.users.api_endpoints.List.serializers import UsersListSerializer
from apps.users.models import User
from apps.common.permissions import IsSuperAdmin


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.FormParser,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ('id', 'role', 'region', 'district',)
    search_fields = ('email', 'profil__name', 'profil__surname',)