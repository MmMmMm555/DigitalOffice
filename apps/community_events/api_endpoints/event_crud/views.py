from rest_framework.generics import (CreateAPIView, ListAPIView,
                        UpdateAPIView, RetrieveAPIView, DestroyAPIView,)
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (CommunityEventsSerializer, CommunityEventsListSerializer,
                          CommunityEventsUpdateSerializer, CommunityEventsDetailSerializer,)
from apps.community_events.models import CommunityEvents
from apps.common.permissions import IsImam, IsDeputy, IsSuperAdmin
from rest_framework.response import Response


class CommunityEventsCreateAPIView(CreateAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class CommunityEventListAPIView(ListAPIView):
    queryset = CommunityEvents.objects.all()
    serializer_class = CommunityEventsListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'type', 'date', 'created_at',)

    def get_queryset(self):
        if self.request.user.role in ['4', '5']:
            return CommunityEvents.objects.filter(imam=self.request.user)
        elif self.request.user.role in ['1']:
            return CommunityEvents.objects.all()
        elif self.request.user.role in ['2']:
            return CommunityEvents.objects.filter(imam__region=self.request.user.region)
        elif self.request.user.role in ['3']:
            return CommunityEvents.objects.filter(imam__district=self.request.user.district)
        return []


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
