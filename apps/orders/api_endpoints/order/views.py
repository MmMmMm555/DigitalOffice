from rest_framework import generics, parsers, permissions
from django.http import HttpResponse

from apps.users.models import Role
from apps.common.permissions import IsSuperAdmin, IsRegionAdmin, IsDistrictAdmin
from .serializers import (DirectionCreateSerializer,
                          DirectionListSerializer,
                          DirectionFilesSerializer,
                          DirectionSingleSerializer,
                          DirectionUpdateSerializer,)
from apps.orders import models
from apps.common.custom_filters import DirectionFilterSet
from apps.common.permissions import IsCreatorOrAdmin
from apps.orders.admin import DirectionsResource


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
    queryset = models.Directions.objects.all().select_related('creator__region', 'creator__district').prefetch_related(
        'to_region', 'to_district', 'required_to_region', 'required_to_district',)
    serializer_class = DirectionListSerializer
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)
    search_fields = ('title',)
    filterset_class = DirectionFilterSet

    def get_queryset(self):
        to_role = self.request.GET.get('to_role')
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        query = self.queryset
        if self.request.user.role != Role.SUPER_ADMIN:
            query = query.filter(creator=self.request.user)
        if to_role:
            query = query.filter(to_role__contains=[to_role])
        if start_date:
            query = query.filter(created_at__gte=start_date)
        if finish_date:
            query = query.filter(created_at__lte=finish_date)
        return query

    def get(self, request, *args, **kwargs):
        excel = self.request.GET.get('excel')
        if excel == 'true':
            query = self.queryset
            for i in self.filterset_fields:
                filters = request.GET.get(i)
                filter = i
                if filters:
                    query = query.filter(**{filter: filters})
            to_role = self.request.GET.get('to_role')
            start_date = self.request.GET.get('start_date')
            finish_date = self.request.GET.get('finish_date')
            if self.request.user.role != Role.SUPER_ADMIN:
                query = query.filter(creator=self.request.user)
            if to_role:
                query = query.filter(to_role__contains=[to_role])
            if start_date:
                query = query.filter(created_at__gte=start_date)
            if finish_date:
                query = query.filter(created_at__lte=finish_date)
            data = DirectionsResource().export(queryset=query)
            response = HttpResponse(data.xlsx, content_type='xlsx')
            response['Content-Disposition'] = "attachment; filename=thesis_data.xlsx"
            return response
        else:
            return self.list(request, *args, **kwargs)


class DirectionUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Directions.objects.all()
    serializer_class = DirectionUpdateSerializer
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser,)
    permission_classes = (IsCreatorOrAdmin,)
    lookup_field = 'pk'


class DirectionSingleView(generics.RetrieveDestroyAPIView):
    queryset = models.Directions.objects.all().select_related('creator', 'creator__profil',).prefetch_related(
        'to_region', 'to_district', 'to_employee', 'required_to_region', 'required_to_district', 'required_to_employee', 'required_to_employee', 'file',)
    serializer_class = DirectionSingleSerializer
    permission_classes = (permissions.IsAuthenticated, IsCreatorOrAdmin,)
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsCreatorOrAdmin(),)
        return (permissions.IsAuthenticated(),)


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
