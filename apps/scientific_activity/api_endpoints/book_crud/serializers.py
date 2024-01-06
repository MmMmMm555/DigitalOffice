from rest_framework.serializers import ModelSerializer, ValidationError

from apps.scientific_activity.models import Book
from apps.scientific_activity.api_endpoints.book_images_api.serializers import BookImageSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'imam', 'name', 'comment', 'images', 'direction', 'date',)


class BookDetailSerializer(ModelSerializer):
    images = BookImageSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'imam', 'name', 'comment', 'images', 'direction', 'date', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation


class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'imam', 'name', 'direction', 'date',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation


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