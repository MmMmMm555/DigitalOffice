from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import date

from apps.orders.models import (DirectionsEmployeeResult,
                                DirectionsEmployeeRead,
                                Directions,
                                ResultImages,
                                ResultVideos,
                                ResultFiles,)


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
                'id': instance.employee.id, 'name': f"{instance.employee.profil.name} {instance.employee.profil.last_name}"}
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
        seen = DirectionsEmployeeRead.objects.filter(employee=instance.employee, direction=instance.direction).first()
        representation['state'] = seen.state if seen else "0"
        representation['direction'] = {
        'id': instance.direction.id, 'title': instance.direction.title, 'direction_type': instance.direction.direction_type, 'types': instance.direction.types, 'from_role': instance.direction.from_role, 'to_role': instance.direction.to_role}
        try:
            representation['employee'] = {
            'id': instance.employee.id, 'name': f"{instance.employee.profil.name} {instance.employee.profil.last_name}", "role": instance.employee.role}
        except:
            representation['employee'] = {'id': instance.employee.id}
        return representation


class DirectionsEmployeeResultSerializer(ModelSerializer):
    class Meta:
        model = DirectionsEmployeeResult
        fields = ('id', 'direction', 'employee',
                  'comment', 'files', 'images', 'videos',)

    def validate(self, attrs):
        # if not DirectionsEmployeeRead.objects.filter(direction=attrs.get('direction'), employee=attrs.get('employee')):
        #     raise ValidationError({'detail': "you can not set result to this direction"})
        direction_date = Directions.objects.get(
            id=attrs.get('direction').id).to_date
        if direction_date < date.today():
            raise ValidationError({'detail': "time expired"})
        return attrs

    def create(self, validated_data):
        result = DirectionsEmployeeResult.objects.create(
            direction=validated_data['direction'],
            employee=validated_data['employee'],
            comment=validated_data.get('comment', 'None'),
        )
        result.images.set(validated_data.get('images', []))
        result.videos.set(validated_data.get('videos', []))
        result.files.set(validated_data.get('files', []))
        result.save()
        DirectionsEmployeeRead.objects.filter(
            direction=result.direction, employee=self.context['request'].user.id).update(state="3")
        if self.context['request'].user.role in ['2', '3', '4', '5']:
            result.employee = self.context['request'].user
            result.save()
        return result
