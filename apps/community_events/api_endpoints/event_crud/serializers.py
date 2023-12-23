from rest_framework.serializers import ModelSerializer, ValidationError

from apps.community_events.models import CommunityEvents
from apps.community_events.api_endpoints.images_api.serializers import ImageSerializer


class CommunityEventsSerializer(ModelSerializer):
    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'type', 'comment', 'images', 'date',)


class CommunityEventsDetailSerializer(ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'type', 'comment', 'images', 'date',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation


class CommunityEventsListSerializer(ModelSerializer):
    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'type', 'comment', 'images', 'date',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation


class CommunityEventsUpdateSerializer(ModelSerializer):
    class Meta:
        model = CommunityEvents
        fields = ('id', 'imam', 'type', 'images', 'comment', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }

    def validate(self, attrs):
        if not self.context['request'].user.id == self.instance.imam.id:
            raise ValidationError('you dont have access to change')
        return attrs
