from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.neighborhood.models import Neighborhood
from .serializers import (NeighborhoodSerializer, NeighborhoodListSerializer,
                          NeighborhoodUpdateSerializer, NeighborhoodDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class NeighborhoodCreateAPIView(CreateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class NeighborhoodListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Neighborhood.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = NeighborhoodListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'participants', 'types',)


class NeighborhoodDetailAPIView(RetrieveAPIView):
    queryset = Neighborhood.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = NeighborhoodDetailSerializer
    permission_classes = (IsAuthenticated,)


class NeighborhoodUpdateAPIView(UpdateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class NeighborhoodDeleteAPIView(DestroyAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
