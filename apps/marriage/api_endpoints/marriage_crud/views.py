from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.marriage.models import Marriage
from .serializers import (MarriageSerializer, MarriageListSerializer,
                          MarriageUpdateSerializer, MarriageDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class MarriageCreateAPIView(CreateAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class MarriageListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Marriage.objects.only('id', 'imam', 'mahr', 'date',).select_related('imam', 'imam__profil',)
    serializer_class = MarriageListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'mahr',)


class MarriageDetailAPIView(RetrieveAPIView):
    queryset = Marriage.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = MarriageDetailSerializer
    permission_classes = (IsAuthenticated,)


class MarriageUpdateAPIView(UpdateAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class MarriageDeleteAPIView(DestroyAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
