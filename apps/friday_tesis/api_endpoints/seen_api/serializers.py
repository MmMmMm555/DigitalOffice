from rest_framework.serializers import ModelSerializer, ValidationError, StringRelatedField

from apps.friday_tesis import models
from apps.orders.models import States



class FridayTesisImamReadSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('id',)

    def save(self):
        tesis = self.instance
        imam = self.context.get('request').user
        if tesis.imam == imam:
            if tesis:
                tesis.state = States.ACCEPTED
                tesis.save()
                return tesis
            raise ValidationError('query not found')
        raise ValidationError('you are not allowed to this action')


class FridayTesisImamReadListSerializer(ModelSerializer):
    mosque = StringRelatedField()
    region = StringRelatedField()
    district = StringRelatedField()
    imam_name = StringRelatedField()
    imam_last_name = StringRelatedField()
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('id', 'tesis', 'imam', 'mosque', 'region', 'district', 'imam_name', 'imam_last_name', 'state', 'requirement', 'created_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['result_id'] = None
        if instance.state == States.DONE:
            try:
                result = models.FridayTesisImamResult.objects.filter(imam=instance.imam, tesis=instance.tesis).last().id
            except:
                result = None
            representation['result_id'] = result
        representation['tesis_title'] = instance.tesis.title
        return representation