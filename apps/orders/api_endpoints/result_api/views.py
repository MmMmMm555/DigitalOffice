from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (DirectionResultVideosSerializer,
                          DirectionResultImagesSerializer,
                          DirectionResultFilesSerializer,
                          DirectionsEmployeeResultSerializer,
                          DirectionsEmployeeResultListSerializer,
                          DirectionsEmployeeResultDetailSerializer,)
from apps.orders.models import (DirectionsEmployeeResult,
                                ResultImages,
                                ResultFiles,
                                ResultVideos,)
from apps.common.permissions import IsSuperAdmin, IsImam, IsRegionAdmin, IsDistrictAdmin, IsDeputy


class DirectionsEmployeeResultView(CreateAPIView):
    queryset = DirectionsEmployeeResult.objects.all()
    serializer_class = DirectionsEmployeeResultSerializer
    permission_classes = (IsImam | IsRegionAdmin | IsDistrictAdmin | IsDeputy,)
    parser_classes = (FormParser, MultiPartParser,)


class DirectionsEmployeeResultListView(ListAPIView):
    queryset = DirectionsEmployeeResult.objects.all().select_related('direction_name')
    serializer_class = DirectionsEmployeeResultListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'direction', 'employee', 'created_at',)

    def get_queryset(self):
        if self.request.user.role == '1':
            return DirectionsEmployeeResult.objects.all()
        return DirectionsEmployeeResult.objects.filter(employee=self.request.user)


class DirectionsEmployeeResultDetailView(ListAPIView):
    queryset = DirectionsEmployeeResult.objects.all()
    serializer_class = DirectionsEmployeeResultDetailSerializer
    permission_classes = (IsAuthenticated,)


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
