from rest_framework.serializers import ModelSerializer

from apps.individual_conversations.api_endpoints.images_crud.serializers import IndividualConversationImageSerializer
from apps.individual_conversations.models import IndividualConversation


class IndividualConversationSerializer(ModelSerializer):
    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'images', 'type', 'title', 'comment', 'date',)


class IndividualConversationDetailSerializer(ModelSerializer):
    images = IndividualConversationImageSerializer(many=True, read_only=True)

    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'images', 'type', 'title',
                  'comment', 'date', 'created_at', 'updated_at',)
        read_only_fields = ('created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None), }
        return representation


class IndividualConversationUpdateSerializer(ModelSerializer):
    class Meta:
        model = IndividualConversation
        fields = ('imam', 'images', 'type', 'title', 'comment', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'images': {'required': False},
            'type': {'required': False},
            'title': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }


class IndividualConversationListSerializer(ModelSerializer):
    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'type', 'title', 'date',)


class IndividualConversationUpdateSerializer(ModelSerializer):
    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'images', 'type', 'title', 'comment', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'type': {'required': False},
            'title': {'required': False},
            'comment': {'required': False},
            'images': {'required': False},
            'date': {'required': False},
        }
