from rest_framework import views, response, generics, parsers, permissions, filters, pagination, viewsets

from django_filters.rest_framework import DjangoFilterBackend


from apps.common.permissions import IsSuperAdmin
from .serializers import FridayTesisSerializer
from apps.friday_tesis import models


class FridayTesisCreateView(generics.CreateAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser)