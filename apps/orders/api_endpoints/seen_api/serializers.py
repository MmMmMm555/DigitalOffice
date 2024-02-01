from rest_framework.serializers import ModelSerializer, ValidationError

from apps.orders import models
from apps.orders.models import States
from apps.friday_tesis.api_endpoints.seen_api.serializers import UserSerializer


class DirectionsEmployeeReadSerializer(ModelSerializer):
    class Meta:
        model = models.DirectionsEmployeeResult
        fields = ('id',)

    def save(self):
        direction = self.instance
        if direction:
            direction.state = States.ACCEPTED
            direction.save()
            return direction
        raise ValidationError('query not found')


class DirectionsEmployeeReadListSerializer(ModelSerializer):
    employee = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.DirectionsEmployeeResult
        fields = ('id', 'direction', 'employee', 'state',
                  'requirement', 'created_at', 'updated_at',)
        read_only_fields = fields
