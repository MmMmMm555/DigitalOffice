from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.users.models import Role
from .serializers import (ResultVideosSerializer,
                          ResultImagesSerializer,
                          FridayTesisImamResultSerializer,
                          FridayTesisImamResultListSerializer,
                          FridayTesisImamResultDetailSerializer,
                          FridayTesisImamResultSerializer,)
from apps.friday_tesis.models import (FridayTesisImamResult,
                                      ResultImages,
                                      ResultVideos,)
from apps.common.permissions import IsSuperAdmin, IsImam


class FridayTesisImamResultView(CreateAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultSerializer
    permission_classes = (IsImam,)
    parser_classes = (FormParser, MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class FridayTesisImamResultListView(ListAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultListSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filterset_fields = ('id', 'tesis', 'imam', 'created_at',)

    def get_queryset(self):
        query = FridayTesisImamResult.objects.all()
        if self.request.user.role == Role.SUPER_ADMIN:
            return query
        return query.filter(imam=self.request.user)


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


class FridayTesisResultDetailView(RetrieveAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultDetailSerializer
    permission_classes = (IsAuthenticated,)


class FridayTesisResultUpdateView(RetrieveUpdateAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsImam,)

    def perform_update(self, serializer):
        if self.request.user == self.get_object().imam:
            serializer.save(imam=self.request.user)
