from rest_framework import generics, parsers

from apps.common.permissions import IsSuperAdmin, IsRegionAdmin, IsDistrictAdmin
from .serializers import (DirectionCreateSerializer,
                          DirectionListSerializer,
                          ValidationError,
                          DirectionSingleSerializer,
                          DirectionUpdateSerializer,)
from apps.orders import models


class DirectionCreateView(generics.CreateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionCreateSerializer
    # permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser,)


class DirectionsListView(generics.ListAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionListSerializer
    # permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    search_fields = ('title',)
    filterset_fields = ('id', 'created_at', 'to_region', 'to_district', 'required_to_region', 'required_to_district', 'to_role', 'from_role', 'types', 'direction_type', 'from_date', 'to_date', )

    # def get_queryset(self):
    #     role = self.request.user.role TODO uncomment
    #     district = self.request.user.district
    #     region = self.request.user.region
    #     model = models.Directions.objects.all()
    #     if role == '3':
    #         return model.filter(from_role=role, to_district=district)
    #     if role == '2':
    #         return model.filter(from_role=role, to_region=region)
    #     if role == '1':
    #         return model
    #     raise ValidationError('user not allowed to this action')

class DirectionDeleteView(generics.DestroyAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionListSerializer
    # permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    lookup_field = 'pk'

class DirectionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionUpdateSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser,)
    # permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    lookup_field = 'pk'

class DirectionSingleView(generics.RetrieveAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionSingleSerializer
    # permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    lookup_field = 'pk'
    
    # def get_queryset(self): TODO uncomment
    #     role = self.request.user.role
    #     district = self.request.user.district
    #     region = self.request.user.region
    #     model = models.Directions.objects.all()
    #     if role == '3':
    #         return model.filter(from_role=role, to_district=district)
    #     if role == '2':
    #         return model.filter(from_role=role, to_region=region)
    #     if role == '1':
    #         return model
    #     return []