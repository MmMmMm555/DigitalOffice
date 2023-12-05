from rest_framework import serializers
from apps.attribute.models import AttributeOption, Attribute


class AttributeSerializer(serializers.ModelSerializer):
    # options = AttributeOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Attribute
        fields = (
            "id",
            "title",
            "image",
            # "options",
            "type",
            "is_required",
            "is_list",
            "order",
        )


class AttributeOptionSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = AttributeOption
        fields = ("id", 'attribute', "title", "order")


class FilterAttributeSerializer(serializers.ModelSerializer):
    options = AttributeOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Attribute
        fields = (
            "id",
            "title",
            "image",
            "options",
            "type",
            "filter_type",
            "is_required",
            "is_list",
            "order",
        )
