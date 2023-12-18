from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import ResultVideos, ResultImages, FridayTesisImamResultSerializer
from apps.friday_tesis.models import FridayTesisImamResult
from apps.common.permissions import IsSuperAdmin, IsImam


class FridayTesisImamResultView(CreateAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultSerializer
    permission_classes = (IsImam,)
    parser_classes = (FormParser, MultiPartParser,)


class FridayTesisImamResultListView(ListAPIView):
    queryset = FridayTesisImamResult.objects.all()
    serializer_class = FridayTesisImamResultSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filterset_fields = ('id', 'tesis', 'imam',)

    def get_queryset(self):
        if self.request.user.role == '4':
            return FridayTesisImamResult.objects.filter(imam=self.request.user)
        elif self.request.user.role == '1':
            return FridayTesisImamResult.objects.all()
        return FridayTesisImamResult.objects.filter(imam=self.request.user)