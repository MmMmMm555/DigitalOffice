from rest_framework.serializers import ModelSerializer, ValidationError
# , BaseSerializer, IntegerField, StringRelatedField

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
        fields = ('id', 'direction', 'employee',
                  'state', 'requirement', 'created_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['direction'] = {
            'id': instance.direction.id, 'title': instance.direction.title, 'direction_type': instance.direction.direction_type, 'types': instance.direction.types, 'from_date': instance.direction.from_date, 'to_date': instance.direction.to_date}
        try:
            representation['employee_name'] = f"{instance.employee.profil.name or None} {instance.employee.profil.last_name or None}"
        except:
            representation['employee_name'] = {instance.employee.username}
        return representation


# class DirectionsUnseenCount(BaseSerializer):
#     count = IntegerField()
#     direction = StringRelatedField()