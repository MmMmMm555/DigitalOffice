from rest_framework.serializers import ModelSerializer

from apps.family_conflicts.models import FamilyConflict


class FamilyConflictSerializer(ModelSerializer):
    class Meta:
        model = FamilyConflict
        fields = ('id', 'imam', 'comment', 'causes', 'types', 'results', 'date',)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None),}
        return representation


class FamilyConflictListSerializer(ModelSerializer):
    class Meta:
        model = FamilyConflict
        fields = ('id', 'imam', 'causes', 'types', 'results', 'date', 'created_at', 'updated_at',)
        read_only_fields = ('created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        imam = getattr(instance, 'imam', None)
        if imam:
            representation['imam'] = {
                'id': getattr(imam, 'id', None),
                'name': f"{getattr(imam.profil, 'name', '')} {getattr(imam.profil, 'last_name', '')}"
            }
        else:
            representation['imam'] = {'id': getattr(imam, 'id', None),}
        return representation

class FamilyConflictUpdateSerializer(ModelSerializer):
    class Meta:
        model = FamilyConflict
        fields = ('id', 'imam', 'comment', 'causes', 'types', 'results', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'causes': {'required': False},
            'types': {'required': False},
            'results': {'required': False},
            'date': {'required': False},
        }