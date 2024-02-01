from apps.orders.models import DirectionsEmployeeResult
from apps.friday_tesis.models import FridayThesisImamResult, States
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderNotification, ThesisNotification


class ThesisNotifications(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FridayThesisImamResult.objects.all()
    serializer_class = ThesisNotification

    def get_queryset(self):
        query = self.queryset.filter(
            state=States.UNSEEN, imam=self.request.user)
        return query


class OrderNotifications(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DirectionsEmployeeResult.objects.all()
    serializer_class = OrderNotification

    def get_queryset(self):
        query = self.queryset.filter(
            state=States.UNSEEN, employee=self.request.user)
        return query
