from rest_framework.serializers import ModelSerializer

from apps.community_events.models import Images


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'image')