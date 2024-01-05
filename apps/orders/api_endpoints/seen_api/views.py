from rest_framework import generics, filters, parsers
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DirectionsEmployeeReadSerializer, DirectionsEmployeeReadListSerializer
from apps.orders import models
from apps.common.permissions import IsSuperAdmin, IsImam


class DirectionEmployeeReadView(generics.UpdateAPIView):
    queryset = models.DirectionsEmployeeRead.objects.all()
    serializer_class = DirectionsEmployeeReadSerializer
    permission_classes = (IsImam,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class DirectionEmployeeReadListView(generics.ListAPIView):
    queryset = models.DirectionsEmployeeRead.objects.all()
    serializer_class = DirectionsEmployeeReadListSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('employee__profil_name', 'direction__title',)
    filterset_fields = ('direction', 'direction__direction_type', 'created_at', 'state', 'requirement', 'employee',)
    
    def get_queryset(self):
        if self.request.user.role == '1':
            return self.queryset
        return self.queryset.filter(employee=self.request.user)