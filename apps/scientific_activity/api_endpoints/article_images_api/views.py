from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleImageSerializer
from apps.scientific_activity.models import Images
from apps.common.permissions import IsImam, IsDeputy


class ArticleImageCreateApiView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ArticleImageSerializer
    parser_classes = [FormParser, MultiPartParser,]
    permission_classes = [IsImam | IsDeputy,]


class ArticleImageListApiView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAuthenticated,]
    filterset_fields = ('id',)
