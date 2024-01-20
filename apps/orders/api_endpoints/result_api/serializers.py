from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date

from apps.orders.models import States
from apps.orders.models import (DirectionsEmployeeResult,
                                DirectionsEmployeeRead,
                                Directions,
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


class DirectionsEmployeeResultListSerializer(ModelSerializer):
    class Meta:
        model = DirectionsEmployeeResult
        fields = ('id', 'direction', 'employee',
                  'comment', 'created_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['direction'] = {
            'id': instance.direction.id, 'title': instance.direction.title, 'direction_type': instance.direction.direction_type}
        try:
            representation['employee'] = {
                'id': instance.employee.id, 'name': f"{instance.employee.profil.first_name} {instance.employee.profil.last_name}"}
        except:
            representation['employee'] = {'id': instance.employee.id}
        return representation


class DirectionsEmployeeResultDetailSerializer(ModelSerializer):
    images = DirectionResultImagesSerializer(many=True, read_only=True)
    videos = DirectionResultVideosSerializer(many=True, read_only=True)
    files = DirectionResultFilesSerializer(many=True, read_only=True)

    class Meta:
        model = DirectionsEmployeeResult
        fields = ('id', 'direction', 'employee',
                  'comment', 'files', 'images', 'videos', 'created_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        seen = DirectionsEmployeeRead.objects.filter(
            employee=instance.employee, direction=instance.direction).first()
        representation['state'] = seen.state if seen else States.UNSEEN
        representation['direction'] = {
            'id': instance.direction.id, 'title': instance.direction.title, 'direction_type': instance.direction.direction_type, 'types': instance.direction.types, 'from_role': instance.direction.from_role, 'to_role': instance.direction.to_role}
        try:
            representation['from'] = f"{instance.employee.profil.mosque.region}, {instance.employee.profil.mosque.district}, {instance.employee.profil.mosque.name}"
            representation['employee'] = {
                'id': instance.employee.id, 'name': f"{instance.employee.profil.first_name} {instance.employee.profil.last_name}", "role": instance.employee.role}
        except:
            representation['from'] = 'Nomalum'
            representation['employee'] = {'id': instance.employee.id}
        return representation


class DirectionsEmployeeResultSerializer(ModelSerializer):
    class Meta:
        model = DirectionsEmployeeResult
        fields = ('id', 'direction', 'employee',
                  'comment', 'files', 'images', 'videos',)

    def validate(self, attrs):
        direction = Directions.objects.filter(
            id=attrs.get('direction').id).last()
        if direction.types == Types.IMPLEMENT:
            direction_date = direction.to_date if direction.to_date else date.today()
            if direction_date < date.today():
                raise ValidationError({'detail': "time expired"})
        return attrs

    def create(self, validated_data):
        result = DirectionsEmployeeResult.objects.create(
            direction=validated_data.get('direction'),
            employee=validated_data.get('employee'),
            comment=validated_data.get('comment', 'None'),
        )
        result.images.set(validated_data.get('images', []))
        result.videos.set(validated_data.get('videos', []))
        result.files.set(validated_data.get('files', []))
        result.save()
        DirectionsEmployeeRead.objects.filter(
            direction=result.direction, employee=self.context['request'].user.id).update(state=States.DONE)
        return result


class DirectionsEmployeeResultUpdateSerializer(ModelSerializer):
    class Meta:
        model = DirectionsEmployeeResult
        fields = ('id', 'direction', 'employee',
                  'comment', 'files', 'images', 'videos',)
        extra_kwargs = {
            'employee': {'required': False},
            'direction': {'required': False},
            }

    def validate(self, attrs):
        if attrs.get('employee') != self.context.get('request').user:
            raise ValidationError({'detail': "you can't update the result"})
        return attrs
