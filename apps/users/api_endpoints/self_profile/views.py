from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSelfSerializer
from apps.users.models import User


class UserSelfView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSelfSerializer
    pagination_class = None
    filter_backends = []
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)
