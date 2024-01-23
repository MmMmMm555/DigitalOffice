from rest_framework.serializers import ModelSerializer, ValidationError

from apps.charity_promotion.models import CharityPromotion
from apps.common.related_serializers import UserRelatedSerializer
from apps.charity_promotion.api_endpoints.images_api.serializers import ImageSerializer


class CharityPromotionSerializer(ModelSerializer):
    class Meta:
        model = CharityPromotion
        fields = ('id', 'imam', 'types', 'participant',
              'help_type', 'from_who', 'comment', 'images', 'date',)


class CharityPromotionListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=False)
    class Meta:
        model = CharityPromotion
        fields = ('id', 'imam', 'types', 'date',)


class CharityPromotionUpdateSerializer(ModelSerializer):
    class Meta:
        model = CharityPromotion
        fields = ('id', 'imam', 'types', 'participant',
                  'help_type', 'from_who', 'comment', 'images', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'help_type': {'required': False},
            'from_who': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }

    def validate(self, attrs):
        if not self.context['request'].user.id == self.instance.imam.id:
            raise ValidationError('you dont have access to change')
        return attrs


class CharityPromotionDetailSerializer(ModelSerializer):
    images = ImageSerializer(many=True)
    imam = UserRelatedSerializer(many=False, read_only=True)
    class Meta:
        model = CharityPromotion
        fields = ('id', 'imam', 'types', 'participant', 'help_type',
                  'from_who', 'comment', 'images', 'date', 'created_at', 'updated_at',)
