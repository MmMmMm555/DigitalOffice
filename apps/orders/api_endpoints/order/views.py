from rest_framework import generics, parsers, permissions

from apps.users.models import Role
from apps.common.permissions import IsSuperAdmin, IsRegionAdmin, IsDistrictAdmin
from .serializers import (DirectionCreateSerializer,
                          DirectionListSerializer,
                          ValidationError,
                          DirectionFilesSerializer,
                          DirectionSingleSerializer,
                          DirectionUpdateSerializer,)
from apps.orders import models
from django.db.models import F


class DirectionCreateView(generics.CreateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionCreateSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user,
                        from_role=self.request.user.role)


class DirectionsListView(generics.ListAPIView):
    """ to_role boyicha filterlash uchun "api/v1/orders/list/?to_role=2" ko'rinishida filter yuboriladi agar multpe filter tanlasa "api/v1/orders/list/?to_role=2&to_role=3" ko'rinishida yuboriladi """
    queryset = models.Directions.objects.all().annotate(
        from_region=F('creator__region__name'), from_district=F('creator__district__name'))
    serializer_class = DirectionListSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    search_fields = ('title',)
    filterset_fields = ('id', 'created_at', 'to_region', 'to_district', 'required_to_region',
                        'required_to_district', 'from_role', 'types', 'direction_type', 'from_date', 'to_date', )

    def get_queryset(self):
        to_role = self.request.GET.get('to_role')
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        query = self.queryset
        if self.request.user.role != Role.SUPER_ADMIN:
            query = query.filter(creator=self.request.user)
        if to_role:
            query = query.filter(to_role__contains=[to_role])
        if start_date and finish_date:
            query = query.filter(created_at__range=[start_date, finish_date])
        elif start_date:
            query = query.filter(created_at__gte=start_date)
        elif finish_date:
            query = query.filter(created_at__lte=finish_date)
        return query


class DirectionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionUpdateSerializer
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser,)
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    lookup_field = 'pk'


class DirectionSingleView(generics.RetrieveDestroyAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionSingleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        if self.request.user.role in [Role.SUPER_ADMIN, Role.REGION_ADMIN, Role.DISTRICT_ADMIN]:
            instance.delete()
        else:
            raise ValidationError({'detail': 'you are not allowed to delete'})


class FileListView(generics.ListAPIView):
    queryset = models.DirectionFiles.objects.all()
    serializer_class = DirectionFilesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = ('id',)


class FileView(generics.CreateAPIView):
    queryset = models.DirectionFiles.objects.all()
    serializer_class = DirectionFilesSerializer
    permission_classes = (IsRegionAdmin | IsDistrictAdmin | IsSuperAdmin,)
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.FileUploadParser,)
