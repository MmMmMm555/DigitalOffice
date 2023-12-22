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
        fields = ('id', 'imam', 'types', 'help_type', 'from_who', 'images', 'summa', 'comment', 'date',)

class CharityUpdateSerializer(ModelSerializer):
    class Meta:
        model = Charity
        fields = ('id', 'imam', 'types', 'help_type', 'from_who', 'summa', 'comment', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'help_type': {'required': False},
            'from_who': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }
    def validate(self, attrs):
        if self.context['request'].user == attrs.get('imam'):
            raise serializers.ValidationError('you dont hav access to change')
        return attrs