from rest_framework import generics, parsers, permissions, filters, response

from django_filters.rest_framework import DjangoFilterBackend


from apps.common.permissions import IsSuperAdmin, IsImam
from .serializers import (FridayTesisSerializer, FridayTesisCreateSerializer,
                          FridayTesisUpdateSerializer, FridayTesisDetailSerializer)
from apps.friday_tesis import models


class FridayTesisCreateView(generics.CreateAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisCreateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser)


class FridayTesisUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisUpdateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser,
                      parsers.FormParser, parsers.FileUploadParser,)


class FridayTesisListView(generics.ListAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title',)
    filterset_fields = ('id', 'date', 'created_at',
                        'to_region', 'to_district',)

    def get_queryset(self):
        if self.request.user.role == '1':
            return self.queryset
        return models.FridayTesis.objects.filter(to_imams=self.request.user)


class FridayTesisDeleteView(generics.DestroyAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisSerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)


class FridayTesisDetailView(generics.RetrieveAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisDetailSerializer
    permission_classes = (IsSuperAdmin|IsImam,)
