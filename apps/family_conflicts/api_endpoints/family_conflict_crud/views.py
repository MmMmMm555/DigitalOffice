from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy
from apps.family_conflicts.models import FamilyConflict
from .serializers import FamilyConflictSerializer, FamilyConflictListSerializer, FamilyConflictUpdateSerializer
from apps.common.view_mixin import FilerQueryByRole


class FamilyConflictCreateAPIView(CreateAPIView):
    queryset = FamilyConflict.objects.all()
    serializer_class = FamilyConflictSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class FamilyConflictListAPIView(FilerQueryByRole, ListAPIView):
    queryset = FamilyConflict.objects.all()
    serializer_class = FamilyConflictListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'created_at', 'causes', 'types', 'results',)


class FamilyConflictDetailAPIView(RetrieveAPIView):
    queryset = FamilyConflict.objects.all()
    serializer_class = FamilyConflictSerializer
    permission_classes = (IsAuthenticated,)


class FamilyConflictUpdateAPIView(UpdateAPIView):
    queryset = FamilyConflict.objects.all()
    serializer_class = FamilyConflictUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)
    
    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:  
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class FamilyConflictDeleteAPIView(DestroyAPIView):
    queryset = FamilyConflict.objects.all()
    serializer_class = FamilyConflictSerializer
    permission_classes = (IsImam | IsDeputy,)
    
    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)