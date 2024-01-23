from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.mavlud.models import Mavlud
from .serializers import (MavludSerializer, MavludListSerializer,
                          MavludUpdateSerializer, MavludDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class MavludCreateAPIView(CreateAPIView):
    queryset = Mavlud.objects.all()
    serializer_class = MavludSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class MavludListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Mavlud.objects.only('id', 'imam', 'title', 'date',).select_related('imam', 'imam__profil',)
    serializer_class = MavludListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date',)


class MavludDetailAPIView(RetrieveAPIView):
    queryset = Mavlud.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = MavludDetailSerializer
    permission_classes = (IsAuthenticated,)


class MavludUpdateAPIView(UpdateAPIView):
    queryset = Mavlud.objects.all()
    serializer_class = MavludUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class MavludDeleteAPIView(DestroyAPIView):
    queryset = Mavlud.objects.all()
    serializer_class = MavludSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
