from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import (ResultVideosSerializer, 
                          ResultImagesSerializer, 
                          FridayTesisImamResultSerializer, 
                          FridayTesisImamResultListSerializer)
from apps.friday_tesis.models import (FridayTesisImamResult,
                                      ResultImages,
                                      ResultVideos,)
from apps.common.permissions import IsSuperAdmin, IsImam


class FridayTesisImamResultView(CreateAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultSerializer
    # permission_classes = (IsImam,)
    parser_classes = (FormParser, MultiPartParser,)


class FridayTesisImamResultListView(ListAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultListSerializer
    # permission_classes = (IsSuperAdmin | IsImam,)
    filterset_fields = ('id', 'tesis', 'imam',)

    def get_queryset(self):
        if self.request.user.role == '1':
            return FridayTesisImamResult.objects.all()
        return FridayTesisImamResult.objects.filter(imam=self.request.user)

class ResultImageView(CreateAPIView):
    queryset = ResultImages.objects.all()
    serializer_class = ResultImagesSerializer
    # permission_classes = (IsImam | IsSuperAdmin,)
    parser_classes = (FormParser, MultiPartParser,)

class ResultImageListView(ListAPIView):
    queryset = ResultImages.objects.all()
    serializer_class = ResultImagesSerializer
    # permission_classes = (IsImam | IsSuperAdmin,)
    filterset_fields = ('id',)

class ResultVideoListView(ListAPIView):
    queryset = ResultVideos.objects.all()
    serializer_class = ResultVideosSerializer
    # permission_classes = (IsImam,)
    filterset_fields = ('id',)

class ResultVideoView(CreateAPIView):
    queryset = ResultVideos.objects.all()
    serializer_class = ResultVideosSerializer
    # permission_classes = (IsImam,)
    parser_classes = (FormParser, MultiPartParser,)