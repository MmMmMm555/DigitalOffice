from rest_framework.serializers import ModelSerializer

from apps.neighborhood.models import Neighborhood
from apps.common.related_serializers import UserRelatedSerializer


class NeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'imam', 'comment', 'participants', 'types', 'date',)


class NeighborhoodDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)
    
    class Meta:
        model = Neighborhood
        fields = ('id', 'imam', 'comment', 'participants',
                  'types', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields



class NeighborhoodListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)
    
    class Meta:
        model = Neighborhood
        fields = ('id', 'imam', 'participants', 'types', 'date',)
        read_only_fields = fields


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
