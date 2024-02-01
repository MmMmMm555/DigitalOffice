from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date
from django.db import transaction

from apps.orders.models import States
from apps.common.related_serializers import UserRelatedSerializer
from apps.orders.models import (DirectionsEmployeeResult,
                                ResultImages,
                                ResultVideos,
                                ResultFiles,
                                Types,)


class DirectionResultImagesSerializer(ModelSerializer):
    class Meta:
        model = ResultImages
        fields = ('id', 'image',)


class DirectionResultVideosSerializer(ModelSerializer):
    class Meta:
        model = ResultVideos
        fields = ('id', 'video',)


class DirectionResultFilesSerializer(ModelSerializer):
    class Meta:
        model = ResultFiles
        fields = ('id', 'file',)


class DirectionsEmployeeResultDetailSerializer(ModelSerializer):
    images = DirectionResultImagesSerializer(many=True, read_only=True)
    videos = DirectionResultVideosSerializer(many=True, read_only=True)
    files = DirectionResultFilesSerializer(many=True, read_only=True)
    employee = UserRelatedSerializer(many=False, read_only=True)

    class Meta:
        model = DirectionsEmployeeResult
        fields = ('id', 'direction', 'employee', 'state',
                  'comment', 'files', 'images', 'videos', 'created_at', 'updated_at',)
        read_only_fields = fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['from'] = f"{instance.employee.profil.mosque.region}, {instance.employee.profil.mosque.district}, {instance.employee.profil.mosque.name}"
        except:
            representation['from'] = None
        return representation


# class DirectionsEmployeeResultSerializer(ModelSerializer):
#     class Meta:
#         model = DirectionsEmployeeResult
#         fields = ('id', 'direction', 'employee',
#                   'comment', 'files', 'images', 'videos',)

#     def validate(self, attrs):
#         direction = Directions.objects.filter(
#             id=attrs.get('direction').id).last()
#         if direction.types == Types.IMPLEMENT:
#             direction_date = direction.to_date if direction.to_date else date.today()
#             if direction_date < date.today():
#                 raise ValidationError({'detail': "time expired"})
#         return attrs

#     def create(self, validated_data):
#         result = DirectionsEmployeeResult.objects.create(
#             direction=validated_data.get('direction'),
#             employee=validated_data.get('employee'),
#             comment=validated_data.get('comment', 'None'),
#         )
#         result.images.set(validated_data.get('images', []))
#         result.videos.set(validated_data.get('videos', []))
#         result.files.set(validated_data.get('files', []))
#         result.save()
#         DirectionsEmployeeRead.objects.filter(
#             direction=result.direction, employee=result.employee).update(state=States.DONE)
#         return result


class DirectionsEmployeeResultUpdateSerializer(ModelSerializer):
    class Meta:
        model = DirectionsEmployeeResult
        fields = ('id', 'comment', 'files', 'images', 'videos',)
        extra_kwargs = {
            'comment': {'required': False},
        }

    def validate(self, attrs):
        direction = self.instance.direction
        if direction.types == Types.IMPLEMENT:
            direction_date = direction.to_date if direction.to_date else date.today()
            if direction_date < date.today():
                raise ValidationError({'detail': "time expired"})
        return attrs

    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.comment = validated_data.get('comment', instance.comment)
            instance.images.set(validated_data.get('images', []))
            instance.videos.set(validated_data.get('videos', []))
            instance.files.set(validated_data.get('files', []))
            instance.state = States.DONE
            instance.save()
            return instance
