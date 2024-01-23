from rest_framework.serializers import ModelSerializer

from apps.marriage.models import Marriage
from apps.common.related_serializers import UserRelatedSerializer


class MarriageSerializer(ModelSerializer):
    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'comment', 'marriage_image',
                  'fhdyo_image', 'mahr', 'date',)


class MarriageDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'comment', 'marriage_image',
                  'fhdyo_image', 'mahr', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class MarriageListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'mahr', 'date',)
        read_only_fields = fields


class MarriageUpdateSerializer(ModelSerializer):
    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'comment', 'marriage_image',
                  'fhdyo_image', 'mahr', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'marriage_image': {'required': False},
            'fhdyo_image': {'required': False},
            'mahr': {'required': False},
            'date': {'required': False},
        }
