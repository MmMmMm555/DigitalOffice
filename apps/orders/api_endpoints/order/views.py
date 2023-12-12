from rest_framework import generics, parsers, permissions, filters

from django_filters.rest_framework import DjangoFilterBackend

from apps.common.permissions import IsSuperAdmin
from .serializers import DirectionSerializer, DirectionCreateSerializer
from apps.orders import models


class DirectionsCreateView(generics.CreateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionCreateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser)


class DirectionsListView(generics.ListAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title',)
    filterset_fields = ('id', 'created_at', 'to_region', 'to_district', 'to_role', 'type', 'direction_type',)