from rest_framework.decorators import api_view
from django.db.models import F, Q, Count

from apps.orders.models import DirectionsEmployeeRead
from apps.friday_tesis.models import FridayThesisImamRead, States
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderNotification, ThesisNotification


# @api_view(['GET'])
# def NotificationApi(request):
#     directions = DirectionsEmployeeRead.objects.filter(
#         state=States.UNSEEN, employee=request.user).values('id', 'direction__title', 'direction__from_role', 'direction__direction_type', 'created_at',)
#     friday_tesis = FridayThesisImamRead.objects.filter(
#         state=States.UNSEEN, imam=request.user).values('id', 'tesis__title', 'created_at',)
#     data = {'count': directions.count()+friday_tesis.count(),
#             'directions': OrderNotification(directions, mant=True), 'friday_tesis': ThesisNotification(friday_tesis, many=True), }
#     return Response(data=data)


class ThesisNotifications(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FridayThesisImamRead.objects.all()
    serializer_class = ThesisNotification

    def get_queryset(self):
        query = self.queryset.filter(
            state=States.UNSEEN, imam=self.request.user)
        return query


class OrderNotifications(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = DirectionsEmployeeRead.objects.all()
    serializer_class = OrderNotification

    def get_queryset(self):
        query = self.queryset.filter(
            state=States.UNSEEN, employee=self.request.user)
        return query
