from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import BookImageSerializer
from apps.scientific_activity.models import BookImages
from apps.common.permissions import IsImam, IsDeputy


class BookImageCreateApiView(CreateAPIView):
    queryset = BookImages.objects.all()
    serializer_class = BookImageSerializer
    parser_classes = [FormParser, MultiPartParser,]
    permission_classes = [IsImam | IsDeputy,]


class BookImageListApiView(ListAPIView):
    queryset = BookImages.objects.all()
    serializer_class = BookImageSerializer
    permission_classes = [IsAuthenticated,]
    filterset_fields = ('id',)
