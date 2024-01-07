from rest_framework import viewsets

from apps.employee.models import Department
from .serializers import DepartmentSerializer


class DepartmentAPIView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_fields = ['id']
    pagination_class = None
    search_fields = ['name']
    lookup_field = 'pk'