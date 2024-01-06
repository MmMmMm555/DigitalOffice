from rest_framework.serializers import ModelSerializer

from apps.scientific_activity.models import BookImages


class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImages
        fields = ('id', 'image')