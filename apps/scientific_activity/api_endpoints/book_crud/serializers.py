from rest_framework.serializers import ModelSerializer, ValidationError

from apps.scientific_activity.models import Book
from apps.scientific_activity.api_endpoints.book_images_api.serializers import BookImageSerializer
from apps.common.related_serializers import UserRelatedSerializer

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'imam', 'name', 'comment', 'images', 'direction', 'date',)


class BookDetailSerializer(ModelSerializer):
    images = BookImageSerializer(many=True)
    imam = UserRelatedSerializer(many=False, read_only=True)
    class Meta:
        model = Book
        fields = ('id', 'imam', 'name', 'comment', 'images', 'direction', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class BookListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)
    class Meta:
        model = Book
        fields = ('id', 'imam', 'name', 'direction', 'date',)
        read_only_fields = fields


class BookUpdateSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'imam', 'name', 'comment', 'images', 'direction', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'comment': {'required': False},
            'name': {'required': False},
            'direction': {'required': False},
            'type': {'required': False},
            'date': {'required': False},
        }

    def validate(self, attrs):
        if not self.context['request'].user.id == self.instance.imam.id:
            raise ValidationError('you dont have access to change')
        return attrs