from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import (DeathSerializer, DeathDetailSerializer,
                          DeathListSerializer, DeathUpdateSerializer,)
from apps.death.models import Death
from apps.common.permissions import IsImam, IsDeputy


class DeathCreateAPIView(CreateAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class DeathListAPIView(ListAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'created_at',)

    def get_queryset(self):
        user_role = self.request.user.role
        if user_role == '4' or user_role == '5':
            return Death.objects.filter(imam=self.request.user)
        elif user_role == '1':
            return Death.objects.all()
        elif user_role == '2':
            return Death.objects.filter(imam__region=self.request.user.region)
        elif user_role == '3':
            return Death.objects.filter(imam__district=self.request.user.district)
        return []


class DeathUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
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
    permission_classes = (IsImam | IsDeputy,)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.imam:
            instance.delete()
            return Response(status=204)
        return Response('you dont have permission')