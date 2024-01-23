from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.religious_advice.models import ReligiousAdvice
from .serializers import (ReligiousAdviceSerializer, ReligiousAdviceListSerializer,
                          ReligiousAdviceUpdateSerializer, ReligiousAdviceDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class ReligiousAdviceCreateAPIView(CreateAPIView):
    queryset = ReligiousAdvice.objects.all()
    serializer_class = ReligiousAdviceSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class ReligiousAdviceListAPIView(FilerQueryByRole, ListAPIView):
    queryset = ReligiousAdvice.objects.only('id', 'imam', 'type','date',).select_related('imam', 'imam__profil',)
    serializer_class = ReligiousAdviceListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'type', 'choices',)


class ReligiousAdviceDetailAPIView(RetrieveAPIView):
    queryset = ReligiousAdvice.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = ReligiousAdviceDetailSerializer
    permission_classes = (IsAuthenticated,)


class ReligiousAdviceUpdateAPIView(UpdateAPIView):
    queryset = ReligiousAdvice.objects.all()
    serializer_class = ReligiousAdviceUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class ReligiousAdviceDeleteAPIView(DestroyAPIView):
    queryset = ReligiousAdvice.objects.all()
    serializer_class = ReligiousAdviceSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
