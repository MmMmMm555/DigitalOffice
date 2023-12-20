from rest_framework import generics, parsers

from apps.common.permissions import IsSuperAdmin, IsRegionAdmin, IsDistrictAdmin
from .serializers import DirectionCreateSerializer
from apps.orders import models


class DirectionCreateView(generics.CreateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionCreateSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser,)


# class DirectionsListView(generics.ListAPIView):
#     queryset = models.Directions.objects.all()
#     serializer_class = DirectionSerializer
#     permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
#     search_fields = ('title',)
#     filterset_fields = ('id', 'created_at', 'to_region', 'to_district', 'to_role', 'type', 'direction_type',)