from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date, timedelta
from django.db import transaction

from apps.orders.models import States
from apps.common.related_serializers import FridayThesisRelatedSerializer, UserRelatedSerializer
from apps.friday_tesis.models import (FridayThesisImamResult,
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


# class FridayThesisImamResultSerializer(ModelSerializer):
#     class Meta:
#         model = FridayThesisImamResult
#         fields = ('id', 'tesis', 'imam', 'comment', 'file', 'child',
#                   'man', 'old_man', 'old', 'images', 'videos', 'created_at',)
#         extra_kwargs = {
#             'child': {'required': True},
#             'man': {'required': True},
#             'old_man': {'required': True},
#             'old': {'required': True},
#         }

#     def validate(self, attrs):
#         if attrs.get('tesis').date + timedelta(days=1) < date.today():
#             raise ValidationError("time expired")
#         return attrs

#     def create(self, validated_data):
#         with transaction.atomic():
#             result = FridayThesisImamResult.objects.create(
#                 tesis=validated_data['tesis'],
#                 imam=validated_data['imam'],
#                 comment=validated_data.get('comment', 'None'),
#                 file=validated_data.get('file'),
#                 child=validated_data.get('child'),
#                 man=validated_data.get('man'),
#                 old_man=validated_data.get('old_man'),
#                 old=validated_data.get('old'),
#             )
#             result.images.set(validated_data.get('images', []))
#             result.videos.set(validated_data.get('videos', []))
#             result.save()
#             FridayThesisImamRead.objects.filter(
#                 tesis=result.tesis, imam=result.imam).update(state=States.DONE)
#             return result


class FridayThesisImamResultDetailSerializer(ModelSerializer):
    images = ResultImagesSerializer(many=True, read_only=True)
    videos = ResultVideosSerializer(many=True, read_only=True)
    tesis = FridayThesisRelatedSerializer(many=False, read_only=True)
    imam = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = FridayThesisImamResult
        fields = ('id', 'tesis', 'imam', 'comment', 'file', 'child', 'state',
                  'man', 'old_man', 'old', 'images', 'videos', 'updated_at',)
        read_only_fields = fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['from'] = f"{instance.imam.profil.mosque.region}, {instance.imam.profil.mosque.district}, {instance.imam.profil.mosque.name}"
        except:
            representation['from'] = None
        return representation


class FridayThesisImamResultUpdateSerializer(ModelSerializer):
    class Meta:
        model = FridayThesisImamResult
        fields = ('id', 'comment', 'file', 'child',
                  'man', 'old_man', 'old', 'images', 'videos',)
        extra_kwargs = {
            'child': {'required': True},
            'man': {'required': True},
            'old_man': {'required': True},
            'old': {'required': True},
        }

    def validate(self, attrs):
        if self.instance.tesis.date+timedelta(days=1) < date.today():
            raise ValidationError("time expired")
        return attrs

    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.comment = validated_data.get('comment', instance.comment)
            instance.file = validated_data.get('file', instance.file)
            instance.child = validated_data.get('child', instance.child)
            instance.man = validated_data.get('man', instance.man)
            instance.old_man = validated_data.get('old_man', instance.old_man)
            instance.old = validated_data.get('old', instance.old)
            instance.state = States.DONE
            instance.images.set(validated_data.get('images', []))
            instance.videos.set(validated_data.get('videos', []))
            instance.save()
            return instance
