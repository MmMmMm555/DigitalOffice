from rest_framework.serializers import ModelSerializer

from apps.individual_conversations.models import IndividualConversationImages


class IndividualConversationImageSerializer(ModelSerializer):
    class Meta:
        model = IndividualConversationImages
        fields = ('id', 'image')