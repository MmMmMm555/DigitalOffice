from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy
from apps.individual_conversations.models import IndividualConversation
from .serializers import (IndividualConversationSerializer, IndividualConversationListSerializer,
                          IndividualConversationUpdateSerializer, IndividualConversationDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class IndividualConversationCreateView(CreateAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class IndividualConversationListView(FilerQueryByRole, ListAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'type', 'created_at',)


class IndividualConversationDetailView(RetrieveAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationDetailSerializer
    permission_classes = (IsAuthenticated,)


class IndividualConversationUpdateView(UpdateAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class IndividualConversationDeleteView(DestroyAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationSerializer
    permission_classes = (IsImam | IsDeputy,)

    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)
