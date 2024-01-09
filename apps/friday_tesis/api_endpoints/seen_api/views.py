from rest_framework import generics, filters, parsers
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F

from .serializers import FridayTesisImamReadSerializer, FridayTesisImamReadListSerializer
from apps.friday_tesis import models
from apps.common.permissions import IsSuperAdmin, IsImam
from apps.users.models import Role


class FridayTesisImamReadView(generics.UpdateAPIView):
    queryset = models.FridayTesisImamRead.objects.all()
    serializer_class = FridayTesisImamReadSerializer
    permission_classes = (IsImam,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class FridayTesisImamReadListView(generics.ListAPIView):
    queryset = models.FridayTesisImamRead.objects.all().annotate(
        mosque=F('imam__profil__mosque__name'), region=F('imam__region__name'), district=F('imam__district__name'), imam_name=F('imam__profil__name'), imam_last_name=F('imam__profil__last_name'))
    serializer_class = FridayTesisImamReadListSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('imam__profil_name', 'tesis__title',)
    filterset_fields = ('tesis', 'created_at', 'state',
                        'tesis__types', 'requirement', 'imom__region', 'imom__district',)

    def get_queryset(self):
        if self.request.user.role == Role.SUPER_ADMIN:
            return self.queryset
        return self.queryset.filter(imam=self.request.user)
