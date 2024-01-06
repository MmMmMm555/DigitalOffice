from rest_framework.generics import ListAPIView

from apps.public_prayers.models import Prayers
from .serializers import PrayersSerializer


class PrayersListAPIView(ListAPIView):
    queryset = Prayers.objects.all()
    serializer_class = PrayersSerializer
    filterset_fields = ['id']