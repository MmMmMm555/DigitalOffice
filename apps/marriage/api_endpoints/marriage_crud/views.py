from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from apps.common.permissions import IsImam, IsDeputy
from apps.marriage.models import Marriage
from .serializers import (MarriageSerializer, MarriageListSerializer, MarriageUpdateSerializer, MarriageDetailSerializer,)


class MarriageCreateAPIView(CreateAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class MarriageListAPIView(ListAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'mahr',)

    def get_queryset(self):
        user_role = self.request.user.role
        if user_role == '4' or user_role == '5':
            return Marriage.objects.filter(imam=self.request.user)
        elif user_role == '1':
            return Marriage.objects.all()
        elif user_role == '2':
            return Marriage.objects.filter(imam__region=self.request.user.region)
        elif user_role == '3':
            return Marriage.objects.filter(imam__district=self.request.user.district)
        return []


class MarriageDetailAPIView(RetrieveAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageDetailSerializer
    permission_classes = (IsAuthenticated,)


class MarriageUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)
    
    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:  
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class MarriageDeleteAPIView(DestroyAPIView):
    queryset = Marriage.objects.all()
    serializer_class = MarriageSerializer
    permission_classes = (IsImam | IsDeputy,)
    
    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)