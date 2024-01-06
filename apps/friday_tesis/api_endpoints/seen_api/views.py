from rest_framework import generics, filters, parsers
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import FridayTesisImamReadSerializer, FridayTesisImamReadListSerializer
from apps.friday_tesis import models
from apps.common.permissions import IsSuperAdmin, IsImam


class FridayTesisImamReadView(generics.UpdateAPIView):
    queryset = models.FridayTesisImamRead.objects.all()
    serializer_class = FridayTesisImamReadSerializer
    permission_classes = (IsImam,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class FridayTesisImamReadListView(generics.ListAPIView):
    queryset = models.FridayTesisImamRead.objects.all()
    serializer_class = FridayTesisImamReadListSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('imam__profil_name', 'tesis__title',)
    filterset_fields = ('tesis', 'created_at', 'state',
                        'tesis__types', 'requirement', 'imam',)

    def get_queryset(self):
        if self.request.user.role == '1':
            return self.queryset
        return self.queryset.filter(imam=self.request.user)
