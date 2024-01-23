from rest_framework.serializers import ModelSerializer, ValidationError

from apps.charity.models import Charity, Images
from apps.common.related_serializers import UserRelatedSerializer


class CharityImageSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'image',)


class CharityCreateSerializer(ModelSerializer):
    class Meta:
        model = Charity
        fields = ('id', 'imam', 'types', 'help_type', 'from_who',
                  'images', 'summa', 'comment', 'date',)


class CharityListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Charity
        fields = ('id', 'imam', 'types', 'date',)
        read_only_fields = fields


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
        if self.context['request'].user == attrs.get('imam'):
            raise ValidationError('you dont have access to change')
        return attrs


class CharityDetailSerializer(ModelSerializer):
    images = CharityImageSerializer(many=True)
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Charity
        fields = ('id', 'imam', 'types', 'help_type', 'from_who', 'images',
                  'summa', 'comment', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields
