from rest_framework.serializers import ModelSerializer

from apps.marriage.models import Marriage


class MarriageSerializer(ModelSerializer):
    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'comment', 'marriage_image', 'marriage_document', 'fhdyo_document', 'fhdyo_image', 'mahr', 'date',)


class MarriageDetailSerializer(ModelSerializer):
    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'comment', 'marriage_image', 'marriage_document', 'fhdyo_document', 'fhdyo_image', 'mahr', 'date', 'created_at', 'updated_at',)

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
            representation['imam'] = {'id': getattr(imam, 'id', None),}
        return representation


class MarriageListSerializer(ModelSerializer):
    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'mahr', 'date',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'first_name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None),}
        return representation

class MarriageUpdateSerializer(ModelSerializer):
    class Meta:
        model = Marriage
        fields = ('id', 'imam', 'comment', 'marriage_image', 'marriage_document', 'fhdyo_document', 'fhdyo_image', 'mahr', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'marriage_image': {'required': False},
            'fhdyo_image': {'required': False},
            'mahr': {'required': False},
            'date': {'required': False},
        }