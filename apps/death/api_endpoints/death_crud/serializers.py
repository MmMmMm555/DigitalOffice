from rest_framework.serializers import ModelSerializer, ValidationError

from apps.death.models import Death


class DeathSerializer(ModelSerializer):
    class Meta:
        model = Death
        fields = ('id', 'imam', 'date', 'image', 'file', 'comment',)


class DeathUpdateSerializer(ModelSerializer):
    class Meta:
        model = Death
        fields = ('id', 'imam', 'date', 'image', 'file', 'comment',)
        extra_kwargs = {
            'imam': {'required': False},
            'date': {'required': False},
            'image': {'required': False},
        }

    def validate(self, attrs):
        if not self.context['request'].user.id == self.instance.imam.id:
            raise ValidationError('you dont have access to change')
        return attrs


class DeathDetailSerializer(ModelSerializer):
    class Meta:
        model = Death
        fields = ('id', 'imam', 'date', 'image', 'file',
                  'comment', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'first_name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None),}
        return representation
        


class DeathListSerializer(ModelSerializer):
    class Meta:
        model = Death
        fields = ('id', 'imam', 'date', 'comment',)
