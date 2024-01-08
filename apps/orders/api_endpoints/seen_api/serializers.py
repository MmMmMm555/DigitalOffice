from rest_framework.serializers import ModelSerializer, ValidationError, StringRelatedField
# , BaseSerializer, IntegerField, StringRelatedField

from apps.orders import models
from apps.orders.models import States


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
    mosque = StringRelatedField()
    region = StringRelatedField()
    district = StringRelatedField()
    employee_name = StringRelatedField()
    employee_last_name = StringRelatedField()

    class Meta:
        model = models.DirectionsEmployeeRead
        fields = ('id', 'direction', 'employee', 'mosque', 'region', 'district', 'employee_name', 'employee_last_name',
                  'state', 'requirement', 'created_at',)

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
        representation['direction'] = {
            'id': instance.direction.id, 'title': instance.direction.title, 'direction_type': instance.direction.direction_type, 'types': instance.direction.types, 'from_date': instance.direction.from_date, 'to_date': instance.direction.to_date}
        return representation


# class DirectionsUnseenCount(BaseSerializer):
#     count = IntegerField()
#     direction = StringRelatedField()
