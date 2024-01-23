from rest_framework.serializers import ModelSerializer

from apps.wedding.models import Wedding
from apps.common.related_serializers import UserRelatedSerializer


class WeddingSerializer(ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)


class WeddingDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'comment', 'types',
                  'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class WeddingListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'types', 'date',)
        read_only_fields = fields


class WeddingUpdateSerializer(ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'title': {'required': False},
            'date': {'required': False},
        }
