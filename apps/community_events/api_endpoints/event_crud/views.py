from rest_framework.generics import (CreateAPIView, ListAPIView,
                        UpdateAPIView, RetrieveAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (CommunityEventsSerializer, CommunityEventsListSerializer,
                          CommunityEventsUpdateSerializer, CommunityEventsDetailSerializer,)
from apps.community_events.models import CommunityEvents
from apps.common.permissions import IsImam, IsDeputy, IsSuperAdmin
from rest_framework.response import Response
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
    permission_classes = (IsSuperAdmin | IsImam | IsDeputy,)

    def delete(self, request, *args, **kwargs):
        if request.user == self.get_object().imam:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        return Response(status=403)


class CommunityEventsUpdateAPIView(UpdateAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsUpdateSerializer
    permission_classes = (IsSuperAdmin | IsImam | IsDeputy,)
    parser_classes = (FormParser,)
