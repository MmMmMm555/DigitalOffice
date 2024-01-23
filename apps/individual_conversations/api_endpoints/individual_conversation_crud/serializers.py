from rest_framework.serializers import ModelSerializer

from apps.individual_conversations.api_endpoints.images_crud.serializers import IndividualConversationImageSerializer
from apps.individual_conversations.models import IndividualConversation
from apps.common.related_serializers import UserRelatedSerializer


class IndividualConversationSerializer(ModelSerializer):
    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'images', 'types', 'title', 'comment', 'date',)


class IndividualConversationDetailSerializer(ModelSerializer):
    images = IndividualConversationImageSerializer(many=True, read_only=True)
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'images', 'types', 'title',
                  'comment', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class IndividualConversationListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'types', 'title', 'date',)
        read_only_fields = fields


class IndividualConversationUpdateSerializer(ModelSerializer):
    class Meta:
        model = IndividualConversation
        fields = ('id', 'imam', 'images', 'types', 'title', 'comment', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'types': {'required': False},
            'title': {'required': False},
            'comment': {'required': False},
            'images': {'required': False},
            'date': {'required': False},
        }
