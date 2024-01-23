from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from apps.charity_promotion.models import CharityPromotion
from apps.common.permissions import IsImam, IsDeputy, IsOwner
from .serializers import (CharityPromotionSerializer, CharityPromotionDetailSerializer,
                          CharityPromotionUpdateSerializer, CharityPromotionListSerializer)
from apps.common.view_mixin import FilerQueryByRole


class CharityPromotionCreateView(CreateAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class CharityPromotionListView(FilerQueryByRole, ListAPIView):
    queryset = CharityPromotion.objects.only('id', 'imam', 'types', 'date',).select_related('imam', 'imam__profil',)
    serializer_class = CharityPromotionListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'types', 'participant',
                        'help_type', 'from_who', 'date',)


class CharityPromotionDetailView(RetrieveAPIView):
    queryset = CharityPromotion.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = CharityPromotionDetailSerializer
    permission_classes = (IsAuthenticated,)


class CharityPromotionUpdateView(UpdateAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class CharityPromotionDeleteView(DestroyAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionDetailSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
