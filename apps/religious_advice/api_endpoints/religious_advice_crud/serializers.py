from rest_framework.serializers import ModelSerializer

from apps.religious_advice.models import ReligiousAdvice


class ReligiousAdviceSerializer(ModelSerializer):
    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'choices', 'comment', 'date',)


class ReligiousAdviceDetailSerializer(ModelSerializer):
    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'choices', 'comment', 'date', 'created_at', 'updated_at',)

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


class ReligiousAdviceListSerializer(ModelSerializer):
    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'choices','date',)


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


class ReligiousAdviceUpdateSerializer(ModelSerializer):
    class Meta:
        model = ReligiousAdvice
        fields = ('id', 'imam', 'type', 'choices', 'comment', 'date',)

        extra_kwargs = {
            'imam': {'required': False},
            'type': {'required': False},
            'choices': {'required': False},
            'comment': {'required': False},
            'date': {'required': False},
        }
