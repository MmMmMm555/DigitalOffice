from rest_framework import serializers

from apps.mosque.models import Mosque, MosqueAttributeOptionValue, MosqueAttributeValue
from apps.attribute.serializers import AttributeSerializer, AttributeOptionSerializer


class MosqueAttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = MosqueAttributeValue
        fields = [
            # 'mosque',
            'attribute',
            'value'
        ]


class MosqueAttributeOptionValueSerializer(serializers.ModelSerializer):
    attribute = AttributeOptionSerializer()

    class Meta:
        model = MosqueAttributeOptionValue
        fields = [
            # 'mosque',
            'attribute',
        ]


class MosqueMainSerailizer(serializers.ModelSerializer):
    attribute_values = MosqueAttributeValueSerializer(many=True)
    attribute_value_options = MosqueAttributeOptionValueSerializer(many=True)

    class Meta:
        model = Mosque
        fields = [
            'title',
            'address',
            'location',
            'built_at',
            'registered_at',
            'mosque_type',
            'mosque_status',

            'attribute_values',
            'attribute_value_options',
        ]
