from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (DirectionResultVideosSerializer,
                          DirectionResultImagesSerializer,
                          DirectionResultFilesSerializer,
                          DirectionsEmployeeResultDetailSerializer,
                          DirectionsEmployeeResultUpdateSerializer,)
from apps.orders.models import (DirectionsEmployeeResult,
                                ResultImages,
                                ResultFiles,
                                ResultVideos,)
from apps.common.permissions import IsImam, IsRegionAdmin, IsDistrictAdmin, IsDeputy, IsDirectionResultOwner


# class DirectionsEmployeeResultView(CreateAPIView):
#     queryset = DirectionsEmployeeResult.objects.all()
#     serializer_class = DirectionsEmployeeResultSerializer
#     permission_classes = (IsImam | IsRegionAdmin |
#                           IsDistrictAdmin | IsDeputy,)
#     parser_classes = (FormParser, MultiPartParser,)

#     def perform_create(self, serializer):
#         serializer.save(employee=self.request.user)


class DirectionsEmployeeResultDetailView(RetrieveAPIView):
    queryset = DirectionsEmployeeResult.objects.all(
    ).select_related('employee', 'employee__profil',).prefetch_related('images', 'files', 'videos',)
    serializer_class = DirectionsEmployeeResultDetailSerializer
    permission_classes = (IsAuthenticated,)


class DirectionsEmployeeResultUpdateView(RetrieveUpdateAPIView):
    queryset = DirectionsEmployeeResult.objects.all()
    serializer_class = DirectionsEmployeeResultUpdateSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (
        (IsImam | IsRegionAdmin | IsDistrictAdmin | IsDeputy), IsDirectionResultOwner,)


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
