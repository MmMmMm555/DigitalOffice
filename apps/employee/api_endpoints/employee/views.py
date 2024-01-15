from rest_framework import generics, parsers, permissions, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from django.db.models import Q

from . import serializers
from apps.common.permissions import IsSuperAdmin, Role
from apps.employee import models


class EmployeeListView(generics.ListAPIView):
    """ hodimlarni yosh boyicha filter qilish uchun "start_age" va "finish_age" filterlariga qiymat yuboriladi, "start_age < finish_age" ! """
    """  "graduated_year"  boyicha filter bor 'yyyy' formatda qiymat yuboriladi sample: "api/v1/employee/employee/list?graduated_year=1000" """
    """ xodimga akkaunt ulangan mi yo'qmi bilish uchun 'has_account' ga true false valuelarni jo'natasiz true da akkaunt ulanganlar false da ulanmagan xodimlar listini qaytaradi """
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeListSerializer
    permission_classes = (IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('name', 'surname', 'last_name',)
    filterset_fields = ('id', 'education', 'position', 'position__department',
                        'academic_degree', 'profile__role', 'mosque__region', 'mosque__district', 'graduated_univer',)

    def get_queryset(self):
        graduated_year = self.request.GET.get('graduated_year')
        start_age = self.request.GET.get('start_age')
        profile = self.request.GET.get('has_account')
        finish_age = self.request.GET.get('finish_age')
        query = models.Employee.objects.all()
        if graduated_year:
            query = query.filter(graduated_year__year=graduated_year)
        if profile:
            if profile == 'false':
                query = query.exclude(profile__isnull=True)
            elif profile == 'true':
                query = query.filter(profile__isnull=False)
        if start_age and finish_age and start_age < finish_age:
            current_year = date.today().year
            start_year = current_year-int(finish_age)
            finish_year = current_year-int(start_age)
            query = query.filter(birth_date__year__range=[
                                 start_year, finish_year])
        return query


class EmployeeCreateView(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser)
    permission_classes = (IsSuperAdmin,)


class EmployeeUpdateView(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeUpdateSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,)
    permission_classes = (IsSuperAdmin,)


class EmployeeDetailView(generics.RetrieveDestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    permission_classes = (IsSuperAdmin,)


class SocialMediaView(viewsets.ModelViewSet):
    queryset = models.SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer
    pagination_class = None
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'employee', 'social_media',)
    lookup_field = 'pk'
