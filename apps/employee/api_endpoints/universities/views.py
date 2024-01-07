from rest_framework.generics import ListAPIView

from apps.employee.models import Graduation
from .serializers import GraduationSerializer


class GraduationAPIView(ListAPIView):
    queryset = Graduation.objects.all()
    serializer_class = GraduationSerializer
    pagination_class = None
    filterset_fields = ['id']
    search_fields = ['name']