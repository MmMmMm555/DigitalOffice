from rest_framework.serializers import ModelSerializer

from apps.family_conflicts.models import FamilyConflict
from apps.common.related_serializers import UserRelatedSerializer


class FamilyConflictSerializer(ModelSerializer):
    class Meta:
        model = FamilyConflict
        fields = ('id', 'imam', 'comment', 'causes',
                  'types', 'results', 'date',)


class FamilyConflictDetailSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = FamilyConflict
        fields = ('id', 'imam', 'comment', 'causes', 'types',
                  'results', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class FamilyConflictListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = FamilyConflict
        fields = ('id', 'imam', 'types', 'date',)
        read_only_fields = fields


class FamilyConflictUpdateSerializer(ModelSerializer):
    class Meta:
        model = FamilyConflict
        fields = ('id', 'imam', 'comment', 'causes',
                  'types', 'results', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'causes': {'required': False},
            'types': {'required': False},
            'results': {'required': False},
            'date': {'required': False},
        }
