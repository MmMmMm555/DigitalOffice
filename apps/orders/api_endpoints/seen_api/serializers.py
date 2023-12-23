from rest_framework.serializers import ModelSerializer, ValidationError

from apps.orders import models


class DirectionsEmployeeReadSerializer(ModelSerializer):
    class Meta:
        model = models.DirectionsEmployeeRead
        fields = ('state',)

    def save(self):
        direction = self.instance
        employee = self.context.get('request').user
        if direction.employee == employee:
            if direction:
                direction.state = self.validated_data['state']
                direction.save()
                return direction
            raise ValidationError('query not found')
        raise ValidationError('you are not allowed to this action')


class DirectionsEmployeeReadListSerializer(ModelSerializer):
    class Meta:
        model = models.DirectionsEmployeeRead
        fields = ('id', 'direction', 'employee', 'state', 'requirement', 'created_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['employee_name'] = f"{instance.employee.profil.name or None} {instance.employee.profil.last_name or None}"
        except:
            representation['employee_name'] = None
        representation['direction_title'] = instance.direction.title
        return representation