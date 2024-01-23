from rest_framework.serializers import ModelSerializer, ValidationError

from apps.death.models import Death
from apps.common.related_serializers import UserRelatedSerializer


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
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Death
        fields = ('id', 'imam', 'date', 'image', 'file',
                  'comment', 'created_at', 'updated_at',)
        read_only_fields = fields


class DeathListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Death
        fields = ('id', 'imam', 'date',)
        read_only_fields = fields
