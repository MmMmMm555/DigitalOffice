from rest_framework.serializers import ModelSerializer

from apps.ceremony.models import Ceremony


class CeremonySerializer(ModelSerializer):
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)


class CeremonyDetailSerializer(ModelSerializer):
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date', 'created_at', 'updated_at',)

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


class CeremonyListSerializer(ModelSerializer):
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'types', 'date',)


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


class CeremonyUpdateSerializer(ModelSerializer):
    class Meta:
        model = Ceremony
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'title': {'required': False},
            'date': {'required': False},
        }
