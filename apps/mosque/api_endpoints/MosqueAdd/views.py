from rest_framework import generics

from apps.mosque.api_endpoints.MosqueGet.serializers import MosqueMainSerailizer
from apps.mosque.models import Mosque


class MosqueCreateAPIView(generics.CreateAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueMainSerailizer


# class MosqueAttributeValueCreateAPIView(generics.CreateAPIView):
