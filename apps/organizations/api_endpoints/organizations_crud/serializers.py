from rest_framework.serializers import ModelSerializer

from apps.organizations.models import Organization
from apps.common.related_serializers import UserRelatedSerializer


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'imam', 'description', 'type', 'prisoner_type',
                  'institution_type', 'participant_type', 'date',)


class OrganizationDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'imam', 'description', 'type', 'prisoner_type',
                  'institution_type', 'participant_type', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class OrganizationListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'imam', 'type', 'date',)
        read_only_fields = fields


class OrganizationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'imam', 'description', 'type', 'prisoner_type',
                  'institution_type', 'participant_type', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'participant_type': {'required': False},
            'description': {'required': False},
            'date': {'required': False},
            'type': {'required': False},
        }
