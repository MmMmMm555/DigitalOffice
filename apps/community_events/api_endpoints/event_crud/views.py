from rest_framework.generics import (CreateAPIView, ListAPIView,
                        UpdateAPIView, RetrieveAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (CommunityEventsSerializer, CommunityEventsListSerializer,
                          CommunityEventsUpdateSerializer, CommunityEventsDetailSerializer,)
from apps.community_events.models import CommunityEvents
from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.common.view_mixin import FilerQueryByRole


class CommunityEventsCreateAPIView(CreateAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class CommunityEventListAPIView(FilerQueryByRole, ListAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'types', 'date', 'created_at',)


class CommunityEventsDetailAPIView(RetrieveAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsDetailSerializer
    permission_classes = (IsAuthenticated,)


class CommunityEventsDeleteAPIView(DestroyAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)


class CommunityEventsUpdateAPIView(UpdateAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsUpdateSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    parser_classes = (FormParser,)

    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)