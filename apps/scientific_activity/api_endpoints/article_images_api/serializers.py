from rest_framework.serializers import ModelSerializer

from apps.scientific_activity.models import Images


class ArticleImageSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'image')