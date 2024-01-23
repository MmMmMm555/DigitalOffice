from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.public_prayers.models import PublicPrayers
from .serializers import (PublicPrayersSerializer, PublicPrayersListSerializer,
                          PublicPrayersUpdateSerializer, PublicPrayersDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole
from apps.common.custom_filters import PublicPrayersFilterSet


class PublicPrayersCreateAPIView(CreateAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class PublicPrayersListAPIView(FilerQueryByRole, ListAPIView):
    queryset = PublicPrayers.objects.only('id', 'imam', 'prayer', 'created_at',).select_related('imam', 'imam__profil',)
    serializer_class = PublicPrayersListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_class = PublicPrayersFilterSet


class PublicPrayersDetailAPIView(RetrieveAPIView):
    queryset = PublicPrayers.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = PublicPrayersDetailSerializer
    permission_classes = (IsAuthenticated,)


class PublicPrayersUpdateAPIView(UpdateAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class PublicPrayersDeleteAPIView(DestroyAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
