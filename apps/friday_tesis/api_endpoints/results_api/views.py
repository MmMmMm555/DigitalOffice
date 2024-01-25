from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import (ResultVideosSerializer,
                          ResultImagesSerializer,
                          FridayThesisImamResultSerializer,
                          FridayThesisImamResultDetailSerializer,
                          FridayThesisImamResultUpdateSerializer,)
from apps.friday_tesis.models import (FridayThesisImamResult,
                                      ResultImages,
                                      ResultVideos,)
from apps.common.permissions import IsSuperAdmin, IsImam, IsOwner


class FridayThesisImamResultView(CreateAPIView):
    queryset = FridayThesisImamResult.objects.all()
    serializer_class = FridayThesisImamResultSerializer
    permission_classes = (IsImam,)
    parser_classes = (FormParser, MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class ResultImageView(CreateAPIView):
    queryset = ResultImages.objects.all()
    serializer_class = ResultImagesSerializer
    permission_classes = (IsImam | IsSuperAdmin,)
    parser_classes = (FormParser, MultiPartParser,)


class ResultImageListView(ListAPIView):
    queryset = ResultImages.objects.all()
    serializer_class = ResultImagesSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id',)


class ResultVideoListView(ListAPIView):
    queryset = ResultVideos.objects.all()
    serializer_class = ResultVideosSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id',)


class ResultVideoView(CreateAPIView):
    queryset = ResultVideos.objects.all()
    serializer_class = ResultVideosSerializer
    permission_classes = (IsImam,)
    parser_classes = (FormParser, MultiPartParser,)


class FridayThesisResultDetailView(RetrieveAPIView):
    queryset = FridayThesisImamResult.objects.all().select_related('imam',
                                                                   'imam__profil', 'tesis',)
    serializer_class = FridayThesisImamResultDetailSerializer
    permission_classes = (IsAuthenticated,)


class FridayThesisResultUpdateView(RetrieveUpdateAPIView):
    queryset = FridayThesisImamResult.objects.all()
    serializer_class = FridayThesisImamResultUpdateSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsOwner, IsImam,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)
