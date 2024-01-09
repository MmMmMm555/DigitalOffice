from rest_framework import generics, parsers, permissions
from datetime import date

from apps.users.models import Role
from apps.common.permissions import IsSuperAdmin, IsRegionAdmin, IsDistrictAdmin
from .serializers import (DirectionCreateSerializer,
                          DirectionListSerializer,
                          ValidationError,
                          DirectionFilesSerializer,
                          DirectionSingleSerializer,
                          DirectionUpdateSerializer,)
from apps.orders import models


class DirectionCreateView(generics.CreateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionCreateSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user,
                        from_role=self.request.user.role)


class DirectionsListView(generics.ListAPIView):
    """ to_role boyicha filterlash uchun "api/v1/orders/list/?to_role=2" ko'rinishida filter yuboriladi """
    queryset = models.Directions.objects.all()
    serializer_class = DirectionListSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    search_fields = ('title',)
    filterset_fields = ('id', 'created_at', 'to_region', 'to_district', 'required_to_region',
                        'required_to_district', 'from_role', 'types', 'direction_type', 'from_date', 'to_date', )

    def get_queryset(self):
        # today = date.today()
        to_role = self.request.GET.get('to_role')
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        query = models.Directions.objects.all()
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


class DirectionDeleteView(generics.DestroyAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionListSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    lookup_field = 'pk'


class DirectionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionUpdateSerializer
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser,)
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    lookup_field = 'pk'


class DirectionSingleView(generics.RetrieveAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionSingleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'

    # def get_queryset(self):
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
    #     return model


class FileListView(generics.ListAPIView):
    queryset = models.DirectionFiles.objects.all()
    serializer_class = DirectionFilesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = ('id',)


class FileView(generics.CreateAPIView):
    queryset = models.DirectionFiles.objects.all()
    serializer_class = DirectionFilesSerializer
    permission_classes = (IsRegionAdmin | IsDistrictAdmin | IsSuperAdmin,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser,)
