from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from apps.charity_promotion.models import CharityPromotion
from apps.common.permissions import IsImam, IsDeputy, IsSuperAdmin
from .serializers import CharityPromotionSerializer, CharityPromotionDetailSerializer, CharityPromotionUpdateSerializer


class CharityPromotionCreateView(CreateAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class CharityPromotionListView(ListAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'types', 'participant',
                        'help_type', 'from_who', 'date',)

    def get_queryset(self):
        if self.request.user.role in ['4', '5']:
            return CharityPromotion.objects.filter(imam=self.request.user)
        elif self.request.user.role in ['1']:
            return CharityPromotion.objects.all()
        elif self.request.user.role in ['2']:
            return CharityPromotion.objects.filter(imam__region=self.request.user.region)
        elif self.request.user.role in ['3']:
            return CharityPromotion.objects.filter(imam__district=self.request.user.district)
        return []


class CharityPromotionDetailView(RetrieveAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionDetailSerializer
    permission_classes = (IsAuthenticated,)


class CharityPromotionUpdateView(RetrieveUpdateAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionUpdateSerializer
    permission_classes = (IsImam|IsDeputy|IsSuperAdmin,)
    parser_classes = (FormParser,)


class CharityPromotionDeleteView(DestroyAPIView):
    queryset = CharityPromotion.objects.all()
    serializer_class = CharityPromotionDetailSerializer
    permission_classes = (IsImam|IsDeputy|IsSuperAdmin,)
