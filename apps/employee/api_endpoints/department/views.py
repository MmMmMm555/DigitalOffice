from rest_framework import viewsets

from apps.employee.models import Department, Position
from .serializers import DepartmentSerializer, PositionSerializer


class DepartmentAPIView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_fields = ['id']
    search_fields = ['name']
    lookup_field = 'pk'