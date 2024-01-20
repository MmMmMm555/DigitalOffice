from rest_framework import generics, parsers, filters, serializers

from django_filters.rest_framework import DjangoFilterBackend
from apps.users.models import Role

from apps.common.permissions import IsSuperAdmin, IsImam
from .serializers import (FridayThesisSerializer, FridayThesisCreateSerializer,
                          FridayThesisUpdateSerializer, FridayThesisDetailSerializer)
from apps.friday_tesis import models


class FridayThesisCreateView(generics.CreateAPIView):
    queryset = models.FridayThesis.objects.all()
    serializer_class = FridayThesisCreateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser)


class FridayThesisUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.FridayThesis.objects.all()
    serializer_class = FridayThesisUpdateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser,)


class FridayThesisListView(generics.ListAPIView):
    queryset = models.FridayThesis.objects.all()
    serializer_class = FridayThesisSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title',)
    filterset_fields = ('id', 'date', 'created_at',
                        'to_region', 'to_district', 'types',)

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        query = models.FridayThesis.objects.all()
        if start_date and finish_date:
            query = query.filter(created_at__gte=start_date, created_at__lte=finish_date)
        elif start_date:
            query = query.filter(created_at__gte=start_date)
        elif finish_date:
            query = query.filter(created_at__lte=finish_date)
        return query


class FridayThesisDetailView(generics.RetrieveDestroyAPIView):
    queryset = models.FridayThesis.objects.all()
    serializer_class = FridayThesisDetailSerializer
    permission_classes = (IsSuperAdmin | IsImam,)

    def perform_destroy(self, instance):
        if self.request.user.role == Role.SUPER_ADMIN:
            instance.delete()
        else:
            raise serializers.ValidationError({'detail': 'you are not allowed to delete'})