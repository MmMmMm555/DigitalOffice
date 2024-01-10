from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy
from apps.public_prayers.models import PublicPrayers
from .serializers import (PublicPrayersSerializer, PublicPrayersListSerializer,
                          PublicPrayersUpdateSerializer, PublicPrayersDetailSerializer,)


class PublicPrayersCreateAPIView(CreateAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class PublicPrayersListAPIView(ListAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'prayer',)

    def get_queryset(self):
        user_role = self.request.user.role
        if user_role == '4' or user_role == '5':
            return PublicPrayers.objects.filter(imam=self.request.user)
        elif user_role == '1':
            return PublicPrayers.objects.all()
        elif user_role == '2':
            return PublicPrayers.objects.filter(imam__region=self.request.user.region)
        elif user_role == '3':
            return PublicPrayers.objects.filter(imam__district=self.request.user.district)
        return []


class PublicPrayersDetailAPIView(RetrieveAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersDetailSerializer
    permission_classes = (IsAuthenticated,)


class PublicPrayersUpdateAPIView(UpdateAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class PublicPrayersDeleteAPIView(DestroyAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersSerializer
    permission_classes = (IsImam | IsDeputy,)

    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)
