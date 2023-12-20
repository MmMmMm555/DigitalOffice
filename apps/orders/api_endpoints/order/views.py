from rest_framework import generics, parsers

from apps.common.permissions import IsSuperAdmin, IsRegionAdmin, IsDistrictAdmin
from .serializers import DirectionCreateSerializer, DirectionListSerializer, ValidationError
from apps.orders import models


class DirectionCreateView(generics.CreateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionCreateSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser,)


class DirectionsListView(generics.ListAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionListSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    search_fields = ('title',)
    filterset_fields = ('id', 'created_at', 'to_region', 'to_district', 'required_to_region', 'required_to_district', 'to_role', 'from_role', 'types', 'direction_type', 'from_date', 'to_date', )

    def get_queryset(self):
        role = self.request.user.role
        if role in ['2', '3']:
            return models.Directions.objects.filter(from_role=role)
        if role == '1':
            return models.Directions.objects.all()
        raise ValidationError('user not allowed to this action')

class DirectionDeleteView(generics.DestroyAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionListSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    lookup_field = 'pk'