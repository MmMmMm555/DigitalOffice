from rest_framework.serializers import ModelSerializer

from apps.mavlud.models import Mavlud
from apps.common.related_serializers import UserRelatedSerializer


class MavludSerializer(ModelSerializer):
    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'comment', 'title', 'date',)


class MavludDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'comment', 'title',
                  'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class MavludListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'title', 'date',)
        read_only_fields = fields


class MavludUpdateSerializer(ModelSerializer):
    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'comment', 'title', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'comment': {'required': False},
            'title': {'required': False},
            'date': {'required': False},
        }
