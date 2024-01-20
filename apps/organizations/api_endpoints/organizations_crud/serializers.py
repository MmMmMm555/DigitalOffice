from rest_framework.serializers import ModelSerializer

from apps.organizations.models import Organization


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'imam', 'description', 'prisoner_type', 'institution_type', 'participant_type', 'date',)


class OrganizationDetailSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'imam', 'description', 'prisoner_type', 'institution_type', 'participant_type', 'date', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'first_name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None), }
        return representation


class OrganizationListSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'imam', 'prisoner_type', 'institution_type', 'participant_type', 'date',)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'first_name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None), }
        return representation


class OrganizationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'imam', 'description', 'prisoner_type', 'institution_type', 'participant_type', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'participant_type': {'required': False},
            'description': {'required': False},
            'date': {'required': False},
        }
