from rest_framework.serializers import ModelSerializer, ValidationError

from apps.friday_tesis import models
from apps.orders.models import States



class FridayTesisImamReadSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('state',)

    def save(self):
        tesis = self.instance
        imam = self.context.get('request').user
        if tesis.imam == imam:
            if tesis:
                tesis.state = self.validated_data['state']
                tesis.save()
                return tesis
            raise ValidationError('query not found')
        raise ValidationError('you are not allowed to this action')


class FridayTesisImamReadListSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('id', 'tesis', 'imam', 'state', 'requirement', 'created_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['result_id'] = None
        if instance.state == States.DONE:
            try:
                result = models.FridayTesisImamResult.objects.filter(imam=instance.imam, tesis=instance.tesis).last().id
            except:
                result = None
            representation['result_id'] = result
        try:
            representation['imam_name'] = f"{instance.imam.profil.name} {instance.imam.profil.last_name}"
        except:
            representation['imam_name'] = instance.imam.username
        representation['tesis_title'] = instance.tesis.title
        return representation