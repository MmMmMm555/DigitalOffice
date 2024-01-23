from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.organizations.models import Organization
from .serializers import (OrganizationSerializer, OrganizationListSerializer,
                          OrganizationUpdateSerializer, OrganizationDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class OrganizationCreateAPIView(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class OrganizationListAPIView(FilerQueryByRole, ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_fields = ('id', 'imam', 'date', 'type', 'participant_type',
                        'institution_type', 'participant_type',)


class OrganizationDetailAPIView(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationDetailSerializer
    permission_classes = (IsAuthenticated,)


class OrganizationUpdateAPIView(UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class OrganizationDeleteAPIView(DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
