from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DirectionEmployeeReadSerializer, DirectionEmployeeReadListSerializer
from apps.orders import models
from apps.common.permissions import IsSuperAdmin 


class DirectionsEmployeeReadView(generics.CreateAPIView):
    queryset = models.DirectionsEmployeeRead.objects.all()
    serializer_class = DirectionEmployeeReadSerializer
    permission_classes = (IsSuperAdmin,)


class DirectionsEmployeeReadListView(generics.ListAPIView):
    queryset = models.DirectionsEmployeeRead.objects.all()
    serializer_class = DirectionEmployeeReadListSerializer
    permission_classes = (IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('employee__profil_name',)
    filterset_fields = ('employee', 'created_at', 'seen',)