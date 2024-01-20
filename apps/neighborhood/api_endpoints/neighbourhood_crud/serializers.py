from rest_framework.serializers import ModelSerializer

from apps.neighborhood.models import Neighborhood


class NeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'imam', 'comment', 'participants', 'types', 'date',)


class NeighborhoodDetailSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'imam', 'comment', 'participants',
                  'types', 'date', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        print(imam)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'first_name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None), }
        return representation


class NeighborhoodListSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'imam', 'participants', 'types', 'date',)

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


class NeighborhoodUpdateSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'imam', 'comment', 'participants', 'types', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'participants': {'required': False},
            'types': {'required': False},
            'date': {'required': False},
        }
