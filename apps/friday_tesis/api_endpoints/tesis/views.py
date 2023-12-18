from rest_framework import generics, parsers, permissions, filters

from django_filters.rest_framework import DjangoFilterBackend


from apps.common.permissions import IsSuperAdmin
from .serializers import FridayTesisSerializer, FridayTesisCreateSerializer, FridayTesisUpdateSerializer
from apps.friday_tesis import models


class FridayTesisCreateView(generics.CreateAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisCreateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser)


class FridayTesisUpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisUpdateSerializer
    permission_classes = (IsSuperAdmin,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser, parsers.FileUploadParser)


class FridayTesisListView(generics.ListAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisSerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title',)
    filterset_fields = ('id', 'date', 'created_at', 'to_region', 'to_district',)


class FridayTesisDeleteView(generics.DestroyAPIView):
    queryset = models.FridayTesis.objects.all()
    serializer_class = FridayTesisSerializer
    permission_classes = (permissions.IsAuthenticated, IsSuperAdmin,)