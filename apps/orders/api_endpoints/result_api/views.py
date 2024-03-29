from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (DirectionResultVideosSerializer,
                          DirectionResultImagesSerializer,
                          DirectionResultFilesSerializer,
                          DirectionsEmployeeResultSerializer,
                          DirectionsEmployeeResultListSerializer,
                          DirectionsEmployeeResultDetailSerializer,
                          DirectionsEmployeeResultUpdateSerializer,)
from apps.orders.models import (DirectionsEmployeeResult,
                                ResultImages,
                                ResultFiles,
                                ResultVideos,)
from apps.common.permissions import IsSuperAdmin, IsImam, IsRegionAdmin, IsDistrictAdmin, IsDeputy
from apps.users.models import Role


class DirectionsEmployeeResultView(CreateAPIView):
    queryset = DirectionsEmployeeResult.objects.all()
    serializer_class = DirectionsEmployeeResultSerializer
    permission_classes = (IsImam | IsRegionAdmin |
                      IsDistrictAdmin | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)


class DirectionsEmployeeResultListView(ListAPIView):
    queryset = DirectionsEmployeeResult.objects.all().select_related('direction_name')
    serializer_class = DirectionsEmployeeResultListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('employee__profil__name',
                     'employee__profil__last_name', 'employee__profil__mosque__name',)
    filterset_fields = ('id', 'direction',
                        'direction__direction_type', 'employee', 'created_at',)

    def get_queryset(self):
        query = DirectionsEmployeeResult.objects.all()
        if self.request.user.role == Role.SUPER_ADMIN:
            return query
        return query.filter(employee=self.request.user)


class DirectionsEmployeeResultDetailView(RetrieveAPIView):
    queryset = DirectionsEmployeeResult.objects.all()
    serializer_class = DirectionsEmployeeResultDetailSerializer
    permission_classes = (IsAuthenticated,)


class DirectionsEmployeeResultUpdateView(RetrieveUpdateAPIView):
    queryset = DirectionsEmployeeResult.objects.all()
    serializer_class = DirectionsEmployeeResultUpdateSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsImam | IsRegionAdmin | IsDistrictAdmin | IsDeputy,)

    def perform_update(self, serializer):
        if self.request.user == self.get_object().employee:
            serializer.save(employee=self.request.user)


class ResultImageView(CreateAPIView):
    queryset = ResultImages.objects.all()
    serializer_class = DirectionResultImagesSerializer
    permission_classes = (IsImam | IsRegionAdmin | IsDistrictAdmin | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)


class ResultImageListView(ListAPIView):
    queryset = ResultImages.objects.all()
    serializer_class = DirectionResultImagesSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id',)


class ResultVideoListView(ListAPIView):
    queryset = ResultVideos.objects.all()
    serializer_class = DirectionResultVideosSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id',)


class ResultVideoView(CreateAPIView):
    queryset = ResultVideos.objects.all()
    serializer_class = DirectionResultVideosSerializer
    permission_classes = (IsImam | IsRegionAdmin | IsDistrictAdmin | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)


class ResultFileListView(ListAPIView):
    queryset = ResultFiles.objects.all()
    serializer_class = DirectionResultFilesSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id',)


class ResultFileView(CreateAPIView):
    queryset = ResultFiles.objects.all()
    serializer_class = DirectionResultFilesSerializer
    permission_classes = (IsImam | IsRegionAdmin | IsDistrictAdmin | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser, FileUploadParser,)
