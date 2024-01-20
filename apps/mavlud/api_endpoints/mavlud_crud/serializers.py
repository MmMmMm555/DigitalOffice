from rest_framework.serializers import ModelSerializer

from apps.mavlud.models import Mavlud


class MavludSerializer(ModelSerializer):
    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'comment', 'title', 'date',)


class MavludDetailSerializer(ModelSerializer):
    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'comment', 'title',
                  'date', 'created_at', 'updated_at',)

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


class MavludListSerializer(ModelSerializer):
    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'title', 'date',)

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


class MavludUpdateSerializer(ModelSerializer):
    class Meta:
        model = Mavlud
        fields = ('id', 'imam', 'comment', 'title', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'comment': {'required': False},
            'title': {'required': False},
            'date': {'required': False},
        }
