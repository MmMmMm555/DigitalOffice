from rest_framework.serializers import ModelSerializer

from apps.charity_promotion.models import CharityPromotionImages


class ImageSerializer(ModelSerializer):
    class Meta:
        model = CharityPromotionImages
        fields = ('id', 'image')
        ref_name = 'charity_promotion_image'