from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy
from apps.individual_conversations.models import IndividualConversation
from .serializers import (IndividualConversationSerializer, IndividualConversationListSerializer,
                          IndividualConversationUpdateSerializer, IndividualConversationDetailSerializer,)


class IndividualConversationCreateView(CreateAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class IndividualConversationListView(ListAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'type', 'created_at',)

    def get_queryset(self):
        user_role = self.request.user.role
        if user_role == '4' or user_role == '5':
            return IndividualConversation.objects.filter(imam=self.request.user)
        elif user_role == '1':
            return IndividualConversation.objects.all()
        elif user_role == '2':
            return IndividualConversation.objects.filter(imam__region=self.request.user.region)
        elif user_role == '3':
            return IndividualConversation.objects.filter(imam__district=self.request.user.district)
        return []


class IndividualConversationDetailView(RetrieveAPIView):
    queryset = IndividualConversation.objects.all()
    serializer_class = IndividualConversationDetailSerializer
    permission_classes = (IsAuthenticated,)


class IndividualConversationUpdateView(RetrieveUpdateAPIView):
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
