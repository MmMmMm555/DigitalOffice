from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy
from apps.organizations.models import Organization
from .serializers import (OrganizationSerializer, OrganizationListSerializer,
                          OrganizationUpdateSerializer, OrganizationDetailSerializer,)


class OrganizationCreateAPIView(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class OrganizationListAPIView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'participant_type',
                    'institution_type', 'participant_type',)

    def get_queryset(self):
        user_role = self.request.user.role
        if user_role == '4' or user_role == '5':
            return Organization.objects.filter(imam=self.request.user)
        elif user_role == '1':
            return Organization.objects.all()
        elif user_role == '2':
            return Organization.objects.filter(imam__region=self.request.user.region)
        elif user_role == '3':
            return Organization.objects.filter(imam__district=self.request.user.district)
        return []


class OrganizationDetailAPIView(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationDetailSerializer
    permission_classes = (IsAuthenticated,)


class OrganizationUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class OrganizationDeleteAPIView(DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsImam | IsDeputy,)

    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)
