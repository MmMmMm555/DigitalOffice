from rest_framework import generics, parsers, permissions, filters, viewsets, views
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from django.http import HttpResponse

from apps.employee.admin import EmployeeResource
from . import serializers
from apps.common.permissions import IsSuperAdmin
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
        query = self.queryset
        if graduated_year:
            query = query.filter(graduated_year__year=graduated_year)
        if profile:
            if profile == 'false':
                query = query.filter(profile__isnull=True)
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


class EmployeeExcelData(generics.ListAPIView):
    queryset = models.Employee.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    serializer_class = serializers.EmployeeListSerializer
    permission_classes = (IsSuperAdmin,)
    filterset_fields = ('id', 'education', 'position', 'position__department',
                        'academic_degree', 'profile__role', 'mosque__region', 'mosque__district', 'graduated_univer',)

    def get(self, request):
        data = EmployeeResource().export(queryset=super().get_queryset())
        response = HttpResponse(data.xlsx, content_type='xlsx')
        response['Content-Disposition'] = "attachment; filename=data.xlsx"
        return response

    def get_queryset(self):
        graduated_year = self.request.GET.get('graduated_year')
        start_age = self.request.GET.get('start_age')
        profile = self.request.GET.get('has_account')
        finish_age = self.request.GET.get('finish_age')
        query = self.queryset
        if graduated_year:
            query = query.filter(graduated_year__year=graduated_year)
        if profile:
            if profile == 'false':
                query = query.filter(profile__isnull=True)
            elif profile == 'true':
                query = query.filter(profile__isnull=False)
        if start_age and finish_age and start_age < finish_age:
            current_year = date.today().year
            start_year = current_year-int(finish_age)
            finish_year = current_year-int(start_age)
            query = query.filter(birth_date__year__range=[
                                 start_year, finish_year])
        return query



    # def get(self, request):
        # graduated_year = request.GET.get('graduated_year')
        # start_age = request.GET.get('start_age')
        # profile = request.GET.get('has_account')
        # finish_age = request.GET.get('finish_age')
        # if graduated_year:
        #     query = query.filter(graduated_year__year=graduated_year)
        # if profile:
        #     if profile == 'false':
        #         query = query.filter(profile__isnull=True)
        #     elif profile == 'true':
        #         query = query.filter(profile__isnull=False)
        # if start_age and finish_age and start_age < finish_age:
        #     current_year = date.today().year
        #     start_year = current_year-int(finish_age)
        #     finish_year = current_year-int(start_age)
        #     query = query.filter(birth_date__year__range=[
        #         start_year, finish_year])
        # data = EmployeeResource().export(queryset=self.queryset)
        # response = HttpResponse(data.xlsx, content_type='xlsx')
        # response['Content-Disposition'] = "attachment; filename=data.xlsx"
        # return response

    # def get(self, request):
    #     query = self.get_queryset()
    #     data = EmployeeResource().export(queryset=query)
    #     response = HttpResponse(data.xlsx, content_type='xlsx')
    #     response['Content-Disposition'] = "attachment; filename=data.xlsx"
    #     return response

    # permission_classes =  (IsSuperAdmin,)
    # filterset_fields = ('id', 'education', 'position', 'position__department',)
    # def get(self, request):
    #     query = models.Employee.objects.all()
    #     # filters here

    #     graduated_year = self.request.GET.get('graduated_year')
    #     start_age = self.request.GET.get('start_age')
    #     profile = self.request.GET.get('has_account')
    #     finish_age = self.request.GET.get('finish_age')
    #     query = models.Employee.objects.all()
    #     if graduated_year:
    #         query = query.filter(graduated_year__year=graduated_year)
    #     if profile:
    #         if profile == 'false':
    #             query = query.filter(profile__isnull=True)
    #         elif profile == 'true':
    #             query = query.filter(profile__isnull=False)
    #     if start_age and finish_age and start_age < finish_age:
    #         current_year = date.today().year
    #         start_year = current_year-int(finish_age)
    #         finish_year = current_year-int(start_age)
    #         query = query.filter(birth_date__year__range=[
    #                             start_year, finish_year])
    #     data = EmployeeResource().export(queryset=query)
    #     response = HttpResponse(data.xlsx, content_type='xlsx')
    #     response['Content-Disposition'] = "attachment; filename=data.xlsx"
    #     return response
