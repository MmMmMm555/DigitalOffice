from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy
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
    queryset = ReligiousAdvice.objects.all()
    serializer_class = ReligiousAdviceListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'type', 'choices',)


class ReligiousAdviceDetailAPIView(RetrieveAPIView):
    queryset = ReligiousAdvice.objects.all()
    serializer_class = ReligiousAdviceDetailSerializer
    permission_classes = (IsAuthenticated,)


class ReligiousAdviceUpdateAPIView(UpdateAPIView):
    queryset = ReligiousAdvice.objects.all()
    serializer_class = ReligiousAdviceUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class ReligiousAdviceDeleteAPIView(DestroyAPIView):
    queryset = ReligiousAdvice.objects.all()
    serializer_class = ReligiousAdviceSerializer
    permission_classes = (IsImam | IsDeputy,)

    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)
