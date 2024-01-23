from rest_framework.serializers import ModelSerializer

from apps.religious_advice.models import ReligiousAdvice
from apps.common.related_serializers import UserRelatedSerializer


class ReligiousAdviceSerializer(ModelSerializer):
    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'choices', 'comment', 'date',)


class ReligiousAdviceDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'choices', 'comment',
                  'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class ReligiousAdviceListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'date',)
        read_only_fields = fields


class ReligiousAdviceUpdateSerializer(ModelSerializer):
    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'choices', 'comment', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'type': {'required': False},
            'choices': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }
