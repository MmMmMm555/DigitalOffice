from rest_framework import generics, parsers
from django_filters.rest_framework import DjangoFilterBackend

from apps.common.regions import Regions, Districts
from .serializers import RegionsSerializer, DistrictsSerializer

class RegionListView(generics.ListAPIView):
    queryset = Regions.objects.all()
    parser_classes = (parsers.FormParser,)
    serializer_class = RegionsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id',)
    
    
# class RegionListAPIView(generics.CreateAPIView):
#     queryset = Regions.objects.all()
#     parser_classes = (parsers.FormParser,)
#     serializer_class = RegionsSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ('id',)
    