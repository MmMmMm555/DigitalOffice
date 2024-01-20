from rest_framework.serializers import ModelSerializer

from apps.public_prayers.models import PublicPrayers
from apps.public_prayers.api_endpoints.prayers_api.serializers import PrayersSerializer



class PublicPrayersSerializer(ModelSerializer):
    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer',)


class PublicPrayersDetailSerializer(ModelSerializer):
    prayer = PrayersSerializer(many=True)
    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer', 'created_at', 'updated_at',)

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


class PublicPrayersListSerializer(ModelSerializer):
    prayer = PrayersSerializer(many=True)
    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer', 'created_at',)


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


class PublicPrayersUpdateSerializer(ModelSerializer):
    class Meta:
        model = PublicPrayers
        fields = ('id', 'imam', 'prayer',)

        extra_kwargs = {
            'imam': {'required': False},
            'prayer': {'required': False},
        }
