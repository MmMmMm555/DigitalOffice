from rest_framework.serializers import ModelSerializer, ValidationError

from apps.friday_tesis import models


class FridayTesisImamReadSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('tesis',)
    
    def create(self, validatet_data):
        tesis = validatet_data.get('tesis', None)
        imam = self.context.get('request').user
        try:
            read = models.FridayTesisImamRead.objects.filter(imam=imam, tesis=tesis).first()
            if read:
                read.seen = True
                read.save()
                return read
            raise ValidationError('query not found')
        except:
            raise ValidationError('something went wrogn')


class FridayTesisImamReadListSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('id', 'tesis', 'imam', 'seen',)

    def to_representation(self, instance):
        representation =super().to_representation(instance)
        representation['imam_profile'] = instance.imam.profil
        return representation