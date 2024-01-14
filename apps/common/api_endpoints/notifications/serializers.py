from rest_framework.serializers import ModelSerializer, CharField

from apps.friday_tesis.models import FridayTesisImamRead
from apps.orders.models import DirectionsEmployeeRead




class ThesisNotification(ModelSerializer):
    title = CharField(source='tesis.title')
    class Meta:
        model = FridayTesisImamRead
        fields = ('tesis', 'title', 'created_at',)
    
        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['all_count'] = instance.all_count
            return data


class OrderNotification(ModelSerializer):
    title = CharField(source='direction.title')
    from_role = CharField(source='direction.from_role')
    direction_type = CharField(source='direction.direction_type')
    class Meta:
        model = DirectionsEmployeeRead
        fields = ('direction', 'title', 'direction_type', 'from_role', 'created_at',)