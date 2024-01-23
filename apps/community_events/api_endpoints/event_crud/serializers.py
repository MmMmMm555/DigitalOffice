from rest_framework.serializers import ModelSerializer, ValidationError

from apps.community_events.models import CommunityEvents
from apps.common.related_serializers import UserRelatedSerializer
from apps.community_events.api_endpoints.images_api.serializers import ImageSerializer


class CommunityEventsSerializer(ModelSerializer):
    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'types', 'comment', 'images', 'date',)


class CommunityEventsDetailSerializer(ModelSerializer):
    images = ImageSerializer(many=True)
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'types', 'comment', 'images', 'date',)


class CommunityEventsListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'types', 'date',)


class CommunityEventsUpdateSerializer(ModelSerializer):
    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'types', 'images', 'comment', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }

    def validate(self, attrs):
        if not self.context['request'].user.id == self.instance.imam.id:
            raise ValidationError('you dont have access to change')
        return attrs
