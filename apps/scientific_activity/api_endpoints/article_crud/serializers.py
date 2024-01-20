from rest_framework.serializers import ModelSerializer, ValidationError

from apps.scientific_activity.models import Article
from apps.scientific_activity.api_endpoints.article_images_api.serializers import ArticleImageSerializer


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'comment', 'images', 'url', 'publication', 'publication_type', 'article_types', 'date',)


class ArticleDetailSerializer(ModelSerializer):
    images = ArticleImageSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'comment', 'images', 'url', 'publication', 'publication_type', 'article_types', 'date', 'created_at', 'updated_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.first_name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation


class ArticleListSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'publication_type', 'article_types', 'date',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['imam'] = {
                'id': instance.imam.id, 'name': f"{instance.imam.profil.first_name} {instance.imam.profil.last_name}"}
        except:
            representation['imam'] = None
        return representation


class ArticleUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'imam', 'type', 'comment', 'images', 'url', 'publication', 'publication_type', 'article_types', 'date',)
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