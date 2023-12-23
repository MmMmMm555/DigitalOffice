from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import ImageSerializer
from apps.community_events.models import Images
from apps.common.permissions import IsImam, IsDeputy, IsSuperAdmin


class ImageCreateApiView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [FormParser, MultiPartParser,]
    permission_classes = [IsImam | IsDeputy,]

class ImageListApiView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated,]
    filterset_fields = ('id',)