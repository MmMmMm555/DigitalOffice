from rest_framework.serializers import ModelSerializer

from apps.public_prayers.models import Prayers


class PrayersSerializer(ModelSerializer):
    class Meta:
        model = Prayers
        fields = ('id', 'name', 'label',)