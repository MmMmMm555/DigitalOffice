from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.wedding.models import Wedding
from .serializers import (WeddingSerializer, WeddingListSerializer,
                          WeddingUpdateSerializer, WeddingDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class WeddingCreateAPIView(CreateAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class WeddingListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'types',)


class WeddingDetailAPIView(RetrieveAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingDetailSerializer
    permission_classes = (IsAuthenticated,)


class WeddingUpdateAPIView(UpdateAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class WeddingDeleteAPIView(DestroyAPIView):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
