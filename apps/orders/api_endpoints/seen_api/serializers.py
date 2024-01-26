from rest_framework.serializers import ModelSerializer, ValidationError, StringRelatedField

from apps.orders import models
from apps.orders.models import States
from apps.friday_tesis.api_endpoints.seen_api.serializers import UserSerializer


class DirectionsEmployeeReadSerializer(ModelSerializer):
    class Meta:
        model = models.DirectionsEmployeeRead
        fields = ('id',)

    def save(self):
        direction = self.instance
        employee = self.context.get('request').user
        if direction.employee == employee:
            if direction:
                direction.state = States.ACCEPTED
                direction.save()
                return direction
            raise ValidationError('query not found')
        raise ValidationError('you are not allowed to this action')


class DirectionsEmployeeReadListSerializer(ModelSerializer):
    employee = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.DirectionsEmployeeRead
        fields = ('id', 'direction', 'employee', 'state',
                  'requirement', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['result_id'] = None
        if instance.state == States.DONE:
            try:
                result = models.DirectionsEmployeeResult.objects.filter(
                    employee=instance.employee, direction=instance.direction).first().id
            except:
                result = None
            representation['result_id'] = result
        return representation
