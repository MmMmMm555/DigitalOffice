from rest_framework.serializers import ModelSerializer, ValidationError

from apps.charity_promotion.models import CharityPromotion
from apps.charity_promotion.api_endpoints.images_api.serializers import ImageSerializer


class CharityPromotionSerializer(ModelSerializer):
    class Meta:
        model = CharityPromotion
        fields = ('id', 'imam', 'types', 'participant',
              'help_type', 'from_who', 'comment', 'images', 'date',)


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
    class Meta:
        model = CharityPromotion
        fields = ('id', 'imam', 'types', 'participant', 'help_type',
                  'from_who', 'comment', 'images', 'date', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation
