from rest_framework import generics, parsers, permissions

from apps.mosque.api_endpoints.FireImages.serializers import FireDefenseImageSerializer
from apps.mosque.models import FireDefenseImages
from apps.common.permissions import IsSuperAdmin, IsDistrictAdmin, IsRegionAdmin


class FireDefenseImagesCreateView(generics.CreateAPIView):
    queryset = FireDefenseImages.objects.all()
    serializer_class = FireDefenseImageSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,)
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)


class FireDefenseImagesRetrieveView(generics.RetrieveAPIView):
    queryset = FireDefenseImages.objects.all()
    serializer_class = FireDefenseImageSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FireDefenseImagesListView(generics.ListAPIView):
    queryset = FireDefenseImages.objects.all()
    serializer_class = FireDefenseImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_fields = ('id', 'type',)
