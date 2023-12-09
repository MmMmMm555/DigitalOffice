from rest_framework import views, response, generics, parsers, permissions, filters, pagination, viewsets

from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema

from apps.common.permissions import IsSuperAdmin
from .serializers import FridayTesisSerializer
from apps.friday_tesis import models
from apps.common.openapi_params import region, district


class FridayTesisCreateView(generics.CreateAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser)