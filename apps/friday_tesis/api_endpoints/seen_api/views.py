from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import FridayTesisImamReadSerializer, FridayTesisImamReadListSerializer
from apps.friday_tesis import models
from apps.common.permissions import IsSuperAdmin 


class FridayTesisImamReadView(generics.CreateAPIView):
    queryset = models.FridayTesisImamRead.objects.all()
    serializer_class = FridayTesisImamReadSerializer
    permission_classes = (IsSuperAdmin,)


class FridayTesisImamReadListView(generics.ListAPIView):
    queryset = models.FridayTesisImamRead.objects.all()
    serializer_class = FridayTesisImamReadListSerializer
    permission_classes = (IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('imam__profil_name',)
    filterset_fields = ('tesis', 'created_at', 'seen',)