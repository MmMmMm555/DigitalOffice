from rest_framework.serializers import ModelSerializer, ValidationError
from apps.friday_tesis.models import (FridayTesisImamResult,
                                            ResultImages,
                                            ResultVideos,)


class FridayTesisImamResultSerializer(ModelSerializer):
    class Meta:
        model = FridayTesisImamResult
        fields = ('id', 'tesis', 'imam', 'comment', 'file',)
    
    def create(self, validated_data):
        result = FridayTesisImamResult.objects.create(**validated_data)
        if self.context['request'].user.role == '4':
            result.imam = self.context['request'].user
            result.save()
        return result

class ResultImagesSerializer(ModelSerializer):
    class Meta:
        model = ResultImages
        fields = ('id', 'result', 'image',)


class ResultVideosSerializer(ModelSerializer):
    class Meta:
        model = ResultVideos
        fields = ('id', 'result', 'videos',)