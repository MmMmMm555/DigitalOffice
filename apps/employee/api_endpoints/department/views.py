from rest_framework import viewsets

from apps.employee.models import Department, Position
from .serializers import DepartmentSerializer, PositionSerializer


class DepartmentAPIView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_fields = ['id']
    pagination_class = None
    search_fields = ['name']
    lookup_field = 'pk'


class PositionAPIView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filterset_fields = ['id']
    pagination_class = None
    search_fields = ['name']
    lookup_field = 'pk'