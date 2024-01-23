from rest_framework.serializers import ModelSerializer, ValidationError

from apps.scientific_activity.models import Article
from apps.scientific_activity.api_endpoints.article_images_api.serializers import ArticleImageSerializer
from apps.common.related_serializers import UserRelatedSerializer


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'comment', 'images', 'url',
                  'publication', 'publication_type', 'article_types', 'date',)


class ArticleDetailSerializer(ModelSerializer):
    images = ArticleImageSerializer(many=True)
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'comment', 'images', 'url', 'publication',
                  'publication_type', 'article_types', 'date', 'created_at', 'updated_at',)
        read_only_fields = fields


class ArticleListSerializer(ModelSerializer):
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'date',)
        read_only_fields = fields


class ArticleUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'comment', 'images', 'url',
                  'publication', 'publication_type', 'article_types', 'date',)
        extra_kwargs = {
            'imam': {'required': False},
            'comment': {'required': False},
            'type': {'required': False},
            'date': {'required': False},
        }

    def validate(self, attrs):
        if not self.context['request'].user.id == self.instance.imam.id:
            raise ValidationError('you dont have access to change')
        return attrs
