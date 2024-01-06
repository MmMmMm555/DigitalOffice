from rest_framework import generics, parsers

from apps.common.regions import Regions
from .serializers import RegionsSerializer


class RegionListView(generics.ListAPIView):
    queryset = Regions.objects.all()
    parser_classes = (parsers.FormParser,)
    serializer_class = RegionsSerializer
    search_fields = ('name',)
    filterset_fields = ('id',)


# class RegionListAPIView(generics.CreateAPIView):
#     queryset = Regions.objects.all()
#     parser_classes = (parsers.FormParser,)
#     serializer_class = RegionsSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ('id',)
