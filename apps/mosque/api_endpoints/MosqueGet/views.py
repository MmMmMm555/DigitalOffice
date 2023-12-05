from rest_framework import generics

from apps.mosque.api_endpoints.MosqueGet.serializers import MosqueMainSerailizer
from apps.mosque.models import Mosque

class MosqueListView(generics.ListAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueMainSerailizer