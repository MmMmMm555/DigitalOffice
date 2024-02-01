from rest_framework.serializers import ModelSerializer, CharField

from apps.friday_tesis.models import FridayThesisImamResult
from apps.orders.models import DirectionsEmployeeResult




class ThesisNotification(ModelSerializer):
    title = CharField(source='tesis.title')
    class Meta:
        model = FridayThesisImamResult
        fields = ('tesis', 'title', 'created_at',)


class OrderNotification(ModelSerializer):
    title = CharField(source='direction.title')
    from_role = CharField(source='direction.from_role')
    direction_type = CharField(source='direction.direction_type')
    class Meta:
        model = DirectionsEmployeeResult
        fields = ('direction', 'title', 'direction_type', 'from_role', 'created_at',)