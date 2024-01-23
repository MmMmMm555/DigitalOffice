from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import (DeathSerializer, DeathDetailSerializer,
                          DeathListSerializer, DeathUpdateSerializer,)
from apps.death.models import Death
from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.common.view_mixin import FilerQueryByRole


class DeathCreateAPIView(CreateAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class DeathListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'created_at',)


class DeathUpdateAPIView(UpdateAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class DeathDetailAPIView(RetrieveAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathDetailSerializer
    permission_classes = (IsAuthenticated,)


class DeathDeleteAPIView(DestroyAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathDetailSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
