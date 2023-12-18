from rest_framework.serializers import ModelSerializer
from apps.friday_tesis.models import (FridayTesisImamResult,
                                            ResultImages,
                                            ResultVideos,)


class FridayTesisImamResultSerializer(ModelSerializer):
    class Meta:
        model = FridayTesisImamResult
        fields = ('id', 'tesis', 'imam', 'comment', 'file',)
    
    def save(self):
        result = self.instance
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