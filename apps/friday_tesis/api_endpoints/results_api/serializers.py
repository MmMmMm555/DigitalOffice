from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date, timedelta

from apps.friday_tesis.models import (FridayTesisImamResult,
                                      FridayTesisImamRead,
                                            FridayTesis,
                                            ResultImages,
                                            ResultVideos,)



class ResultImagesSerializer(ModelSerializer):
    class Meta:
        model = ResultImages
        fields = ('id', 'image',)


class ResultVideosSerializer(ModelSerializer):
    class Meta:
        model = ResultVideos
        fields = ('id', 'video',)

class FridayTesisImamResultListSerializer(ModelSerializer):
    images = ResultImagesSerializer(many=True, read_only=True)
    videos = ResultVideosSerializer(many=True, read_only=True)

    class Meta:
        model = FridayTesisImamResult
        fields = ('id', 'tesis', 'imam', 'comment', 'file', 'child', 'man', 'old_man', 'old', 'images', 'videos',)


class FridayTesisImamResultSerializer(ModelSerializer):
    # def validate_file(self, value):
    #     if value.size > settings.MAX_FILE_SIZE:
    class Meta:
        model = FridayTesisImamResult
        fields = ('id', 'tesis', 'imam', 'comment', 'file', 'child', 'man', 'old_man', 'old', 'images', 'videos', 'created_at',)
        extra_kwargs = {
            'child': {'required': True},
            'man': {'required': True},
            'old_man': {'required': True},
            'old': {'required': True}, 
        }
    
    def validate(self, attrs):
        tesis_date = FridayTesis.objects.get(id=attrs.get('tesis').id).date
        if tesis_date+timedelta(days=1) < date.today():
            raise ValidationError("time expired")
        return attrs

    def create(self, validated_data):
        result = FridayTesisImamResult.objects.create(
            tesis = validated_data['tesis'], 
            imam = validated_data['imam'], 
            comment = validated_data.get('comment', 'None'),
            file = validated_data.get('file'),
            child = validated_data.get('child'),
            man = validated_data.get('man'),
            old_man = validated_data.get('old_man'),
            old = validated_data.get('old'),
        )
        result.images.set(validated_data.get('images', []))
        result.videos.set(validated_data.get('videos', []))
        result.save()
        seen = FridayTesisImamRead.objects.filter(tesis=result.tesis, imam=self.context['request'].user.id).update(state="3")
        if self.context['request'].user.role == '4':
            result.imam = self.context['request'].user
            result.save()
        return result