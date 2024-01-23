from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.common.view_mixin import FilerQueryByRole
from apps.ceremony.models import Ceremony
from .serializers import (CeremonySerializer, CeremonyListSerializer,
                          CeremonyUpdateSerializer, CeremonyDetailSerializer,)


class CeremonyCreateAPIView(CreateAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = CeremonySerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class CeremonyListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Ceremony.objects.only('id', 'imam', 'title', 'types', 'date',).select_related('imam', 'imam__profil',)
    serializer_class = CeremonyListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'types',)


class CeremonyDetailAPIView(RetrieveAPIView):
    queryset = Ceremony.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = CeremonyDetailSerializer
    permission_classes = (IsAuthenticated,)


class CeremonyUpdateAPIView(UpdateAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = CeremonyUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class CeremonyDeleteAPIView(DestroyAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = CeremonySerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
