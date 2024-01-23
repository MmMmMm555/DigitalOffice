from rest_framework.serializers import ModelSerializer

from apps.public_prayers.models import PublicPrayers
from apps.public_prayers.api_endpoints.prayers_api.serializers import PrayersSerializer
from apps.common.related_serializers import UserRelatedSerializer


class PublicPrayersSerializer(ModelSerializer):
    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer',)


class PublicPrayersDetailSerializer(ModelSerializer):
    prayer = PrayersSerializer(many=True)
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer', 'created_at', 'updated_at',)
        read_only_fields = fields


class PublicPrayersListSerializer(ModelSerializer):
    prayer = PrayersSerializer(many=True)
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer', 'created_at',)
        read_only_fields = fields


class PublicPrayersUpdateSerializer(ModelSerializer):
    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer',)

        extra_kwargs = {
            'imam': {'required': False},
            'prayer': {'required': False},
        }
