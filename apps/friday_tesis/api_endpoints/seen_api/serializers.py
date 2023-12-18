from rest_framework.serializers import ModelSerializer, ValidationError

from apps.friday_tesis import models


class FridayTesisImamReadSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('tesis',)
    
    def create(self, validated_data):
        tesis = validated_data.get('tesis', None)
        imam = self.context.get('request').user
        try:
            if imam.role == '4':
                read = models.FridayTesisImamRead.objects.filter(imam=imam, tesis=tesis).first()
                if read:
                    read.seen = True
                    read.save()
                    return read
                raise ValidationError('query not found')
            raise ValidationError('unsupported user')
        except:
            raise ValidationError('something went wrong')


class FridayTesisImamReadListSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('id', 'tesis', 'imam', 'seen',)

    def to_representation(self, instance):
        representation =super().to_representation(instance)
        if instance.requirement:
            representation['requirement'] = instance.requirement
        representation['imam_name'] = f"{instance.imam.profil.name} {instance.imam.profil.last_name}"
        representation['tesis_title'] = instance.tesis.title
        return representation