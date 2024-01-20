from rest_framework import generics, parsers
from django.db.models import F

from .serializers import FridayThesisImamReadSerializer, FridayThesisImamReadListSerializer
from apps.friday_tesis import models
from apps.common.permissions import IsSuperAdmin, IsImam
from apps.users.models import Role


class FridayThesisImamReadView(generics.UpdateAPIView):
    queryset = models.FridayThesisImamRead.objects.all()
    serializer_class = FridayThesisImamReadSerializer
    permission_classes = (IsImam,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class FridayThesisImamReadListView(generics.ListAPIView):
    # queryset = models.FridayThesisImamRead.objects.all().annotate(
    #     mosque=F('imam__profil__mosque__name'), region=F('imam__region__name'), district=F('imam__district__name'), imam_name=F('imam__profil__first_name'), imam_last_name=F('imam__profil__last_name'))
    serializer_class = FridayThesisImamReadListSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    search_fields = ('imam__profil__first_name', 'tesis__title',)
    filterset_fields = ('tesis', 'state',
                        'tesis__types', 'requirement', 'imam', 'imam__region', 'imam__profil__mosque', 'imam__district',)

    def get_queryset(self):
        query = models.FridayThesisImamRead.objects.all().annotate(
            mosque=F('imam__profil__mosque__name'), region=F('imam__region__name'), district=F('imam__district__name'), imam_name=F('imam__profil__first_name'), imam_last_name=F('imam__profil__last_name'))
        if self.request.user.role == Role.SUPER_ADMIN:
            return query
        return query.filter(imam=self.request.user)
