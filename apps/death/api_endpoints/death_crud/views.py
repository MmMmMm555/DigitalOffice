from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import (DeathSerializer, DeathDetailSerializer, DeathListSerializer, DeathUpdateSerializer,)
from apps.death.models import Death
from apps.common.permissions import IsImam, IsDeputy


class DeathCreateAPIView(CreateAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathSerializer
    permission_classes = (IsImam|IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)
    
    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class DeathListAPIView(ListAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'date', 'created_at',)
    
    def get_queryset(self):
        if self.request.user.role in ['4', '5']:
            return Death.objects.filter(imam=self.request.user)
        elif self.request.user.role in ['1']:
            return Death.objects.all()
        elif self.request.user.role in ['2']:
            return Death.objects.filter(imam__region=self.request.user.region)
        elif self.request.user.role in ['3']:
            return Death.objects.filter(imam__district=self.request.user.district)
        return []


class DeathUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathUpdateSerializer
    permission_classes = (IsImam|IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)
    
    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class DeathDetailAPIView(RetrieveAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathDetailSerializer
    permission_classes = (IsAuthenticated,)


class DeathDeleteAPIView(DestroyAPIView):
    queryset = Death.objects.all()
    serializer_class = DeathDetailSerializer
    permission_classes = (IsImam|IsDeputy,)
    
    def delete(self, request, *args, **kwargs):
        if request.user == self.get_object().imam:
            instance = self.get_object()
            instance.delete()
            return Response(status=204)
        return Response('you dont have permission')