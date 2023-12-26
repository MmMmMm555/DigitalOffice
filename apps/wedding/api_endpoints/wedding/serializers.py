from rest_framework.serializers import ModelSerializer

from apps.wedding.models import Wedding


class WeddingSerializer(ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)


class WeddingDetailSerializer(ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None), }
        return representation


class WeddingListSerializer(ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'types', 'date',)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None), }
        return representation


class WeddingUpdateSerializer(ModelSerializer):
    class Meta:
        model = Wedding
        fields = ('id', 'imam', 'title', 'comment', 'types', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'title': {'required': False},
            'date': {'required': False},
        }
