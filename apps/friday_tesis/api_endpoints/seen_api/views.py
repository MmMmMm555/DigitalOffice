from rest_framework import generics, permissions

from .serializers import FridayTesisImamReadSerializer
from apps.friday_tesis import models


class FridayTesisImamReadView(generics.CreateAPIView):
    queryset = models.FridayTesisImamRead.objects.all()
    serializer_class = FridayTesisImamReadSerializer
    permission_classes = (permissions.IsAuthenticated,)
    