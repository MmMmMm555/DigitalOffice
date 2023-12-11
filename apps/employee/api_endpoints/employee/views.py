from rest_framework import generics, parsers, permissions, filters, pagination, viewsets
from apps.common.permissions import IsSuperAdmin
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend

from apps.employee import models


class EmployeeListView(generics.ListAPIView):
    queryset = models.Employee.objects.all().prefetch_related('activity', 'socialmedia', 'workactivity')
    serializer_class = serializers.EmployeeListSerializer
    pagination_class = pagination.PageNumberPagination
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('name', 'surname', 'last_name',)
    filterset_fields = ('id', 'birth_date', 'education', 'graduated_year', 'academic_degree',)

class EmployeeCreateView(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    parser_classes = (parsers.FormParser,)
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    
class EmployeeUpdateView(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    parser_classes = (parsers.FormParser,)
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
   
class EmployeeDestroyView(generics.DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)

class ActivityView(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'employee',)

class WorkActivityView(viewsets.ModelViewSet):
    queryset = models.WorkActivity.objects.all()
    serializer_class = serializers.WorkActivitySerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'employee',)

class SocialMediaView(viewsets.ModelViewSet):
    queryset = models.SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'employee',)