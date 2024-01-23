from rest_framework.serializers import ModelSerializer

from apps.ceremony.models import Ceremony
from apps.common.related_serializers import UserRelatedSerializer


class CeremonySerializer(ModelSerializer):
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)


class CeremonyDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date', 'created_at', 'updated_at',)


class CeremonyListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'types', 'date',)
        read_only_fields = fields


class CeremonyUpdateSerializer(ModelSerializer):
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'title': {'required': False},
            'date': {'required': False},
        }
