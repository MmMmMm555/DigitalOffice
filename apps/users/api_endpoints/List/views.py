from rest_framework import generics, filters, permissions, serializers
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse

from apps.users.api_endpoints.List.serializers import (
    UsersListSerializer, UsersDetailSerializer, UsersUpdateSerializer, SelfProfileUpdateSerializer)
from apps.users.models import User, Role
from apps.common.permissions import IsSuperAdmin
from rest_framework.parsers import FormParser, MultiPartParser
from apps.employee.models import Employee
from apps.users.admin import UserResource


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all().exclude(role=Role.SUPER_ADMIN)
    serializer_class = UsersListSerializer
    permission_classes = (IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = ('id', 'role', 'region', 'district', 'profil__mosque',)
    search_fields = ('email', 'profil__first_name', 'profil__middle_name', 'username',)


class UsersDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersDetailSerializer
    permission_classes = (IsSuperAdmin,)


class UsersUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersUpdateSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsSuperAdmin,)


class SelfProfileUpdateView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = SelfProfileUpdateSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_update(self, serializer):
        if self.request.user.profil.id == self.get_object().id:
            serializer.save()
        else:
            raise serializers.ValidationError({'detail': "you are not allowed"})


class UsersExcelData(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer
    permission_classes = (IsSuperAdmin,)
    filterset_fields = ('id', 'role', 'region', 'district', 'profil__mosque',)

    def get(self, request):
        query = self.queryset
        for i in self.filterset_fields:
            filters = request.GET.get(i)
            filter=i
            if filters:
                query = query.filter(**{filter: filters})
        data = UserResource().export(queryset=query)
        response = HttpResponse(data.xlsx, content_type='xlsx')
        response['Content-Disposition'] = "attachment; filename=users_data.xlsx"
        return response