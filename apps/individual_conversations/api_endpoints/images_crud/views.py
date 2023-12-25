from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import IndividualConversationImageSerializer
from apps.individual_conversations.models import IndividualConversationImages
from apps.common.permissions import IsImam, IsDeputy


class ImageCreateApiView(CreateAPIView):
    queryset = IndividualConversationImages.objects.all()
    serializer_class = IndividualConversationImageSerializer
    parser_classes = [FormParser, MultiPartParser,]
    permission_classes = [IsImam | IsDeputy,]

class ImageListApiView(ListAPIView):
    queryset = IndividualConversationImages.objects.all()
    serializer_class = IndividualConversationImageSerializer
    permission_classes = [IsAuthenticated,]
    filterset_fields = ('id',)