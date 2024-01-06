from rest_framework import generics, parsers

from apps.common.regions import Districts
from .serializers import DistrictsSerializer


class DistrictListView(generics.ListAPIView):
    queryset = Districts.objects.all()
    parser_classes = (parsers.FormParser,)
    serializer_class = DistrictsSerializer
    search_fields = ('name',)
    filterset_fields = ('id', 'region',)
