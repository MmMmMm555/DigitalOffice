from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, Role
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


class CeremonyListAPIView(ListAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = CeremonyListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'types',)

    def get_queryset(self):
        query = Ceremony.objects.all()
        user_role = self.request.user.role
        if user_role == Role.IMAM or user_role == Role.SUB_IMAM:
            query = query.filter(imam=self.request.user)
        elif user_role == Role.REGION_ADMIN:
            query = query.filter(imam__region=self.request.user.region)
        elif user_role == Role.DISTRICT_ADMIN:
            query = query.filter(imam__district=self.request.user.district)
        return query


class CeremonyDetailAPIView(RetrieveAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = CeremonyDetailSerializer
    permission_classes = (IsAuthenticated,)


class CeremonyUpdateAPIView(UpdateAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = CeremonyUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class CeremonyDeleteAPIView(DestroyAPIView):
    queryset = Ceremony.objects.all()
    serializer_class = CeremonySerializer
    permission_classes = (IsImam | IsDeputy,)

    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)
