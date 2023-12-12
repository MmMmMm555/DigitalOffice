from rest_framework.serializers import ModelSerializer, ValidationError

from apps.orders import models


class DirectionEmployeeReadSerializer(ModelSerializer):
    class Meta:
        model = models.DirectionsEmployeeRead
        fields = ('direction',)
    
    def create(self, validatet_data):
        direction = validatet_data.get('direction', None)
        employee = self.context.get('request').user
        try:
            read = models.DirectionsEmployeeRead.objects.filter(employee=employee, direction=direction).first()
            if read:
                read.seen = True
                read.save()
                return read
            raise ValidationError('query not found')
        except:
            raise ValidationError('something went wrogn')


class DirectionEmployeeReadListSerializer(ModelSerializer):
    class Meta:
        model = models.DirectionsEmployeeRead
        fields = ('id', 'direction', 'employee', 'seen',)

    def to_representation(self, instance):
        representation =super().to_representation(instance)
        representation['profile'] = instance.employee.profil
        return representation 
    error