from rest_framework import generics, parsers

from .serializers import FridayThesisImamReadSerializer, FridayThesisImamReadListSerializer
from apps.friday_tesis import models
from apps.common.permissions import IsSuperAdmin, IsImam, IsOwner
from apps.users.models import Role


class FridayThesisImamReadView(generics.UpdateAPIView):
    queryset = models.FridayThesisImamResult.objects.all()
    serializer_class = FridayThesisImamReadSerializer
    permission_classes = (IsImam, IsOwner,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class FridayThesisImamReadListView(generics.ListAPIView):
    queryset = models.FridayThesisImamResult.objects.only('id', 'tesis', 'imam', 'state', 'requirement', 'created_at',).select_related(
        'imam', 'imam__profil', 'imam__region', 'imam__district', 'imam__profil__mosque',)
    serializer_class = FridayThesisImamReadListSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    search_fields = ('imam__profil__first_name',
                     'imam__profil__last_name', 'imam__profil__mosque__name',)
    filterset_fields = ('tesis', 'state',
                        'tesis__types', 'imam__region', 'imam__profil__mosque', 'imam__district',)

    def get_queryset(self):
        query = self.queryset
        if self.request.user.role != Role.SUPER_ADMIN:
            return query.filter(imam=self.request.user)
        return query
