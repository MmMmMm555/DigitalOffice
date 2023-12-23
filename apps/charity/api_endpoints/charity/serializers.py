from rest_framework.serializers import ModelSerializer

from apps.charity.models import Charity, Images
from rest_framework import serializers


class CharityImageSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'image',)


class CharityCreateSerializer(ModelSerializer):
    class Meta:
        model = Charity
        fields = ('id', 'imam', 'types', 'help_type', 'from_who',
                  'images', 'summa', 'comment', 'date',)


class CharityUpdateSerializer(ModelSerializer):
    class Meta:
        model = Charity
        fields = ('id', 'imam', 'types', 'help_type',
                  'from_who', 'summa', 'comment', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'help_type': {'required': False},
            'from_who': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }

    def validate(self, attrs):
        if not self.context['request'].user.id == self.instance.imam.id:
            raise serializers.ValidationError('you dont have access to change')
        return attrs


class CharityDetailSerializer(ModelSerializer):
    images = CharityImageSerializer(many=True)

    class Meta:
        model = Charity
        fields = ('id', 'imam', 'types', 'help_type', 'from_who', 'images',
                  'summa', 'comment', 'date', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation
