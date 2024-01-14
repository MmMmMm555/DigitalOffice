from rest_framework.decorators import api_view
from django.db.models import F, Q

from apps.orders.models import DirectionsEmployeeRead
from apps.friday_tesis.models import FridayTesisImamRead, States
from rest_framework.response import Response


@api_view(['GET'])
def NotificationApi(request):
    directions = DirectionsEmployeeRead.objects.filter(
        state=States.UNSEEN, employee=request.user).values('id', 'direction__title', 'direction__from_role', 'direction__direction_type', 'created_at',)
    friday_tesis = FridayTesisImamRead.objects.filter(
        state=States.UNSEEN, imam=request.user).values('id', 'tesis__title', 'created_at',)
    data = {'count': directions.count()+friday_tesis.count(),
            'directions': directions, 'friday_tesis': friday_tesis, }
    return Response(data=data)
