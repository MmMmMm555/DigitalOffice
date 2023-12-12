from rest_framework.serializers import ModelSerializer, ValidationError
from apps.orders import models
from apps.users.models import User
from apps.common.regions import Regions, Districts


class DirectionSerializer(ModelSerializer):
    class Meta:
        model = models.Directions
        fields = ('id',
                  'title',
                  'direction_type',
                  'file',
                  'type',
                  'to_role',
                  'to_region',
                  'to_district',
                  'to_imams',
                  'from_date',
                  'to_date',
                  'created_at',
                  'updated_at',
                  'voice',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['seen_count'] = models.DirectionsEmployeeRead.objects.filter(direction=instance, seen=True).count()
        representation['unseen_count'] = models.DirectionsEmployeeRead.objects.filter(direction=instance, seen=False).count()
        return representation


class DirectionCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Directions
        fields = ('id',
                  'title',
                  'direction_type',
                  'file',
                  'type',
                  'to_role',
                  'to_region',
                  'to_district',
                  'to_imams',
                  'from_date',
                  'to_date',
                  'voice',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )

    def create(self, validated_data):
        try:
            to_role = validated_data.get('to_role'),
            imams = User.objects.filter(role=to_role[0])
            imam_list = validated_data.get('to_imams', None)
            district_list = validated_data.get('to_district', None)
            region_list = validated_data.get('to_region', None)
            
            direction = models.Directions.objects.create(
                title = validated_data.get('title'),
                direction_type = validated_data.get('direction_type'),
                file = validated_data.get('file'),
                type = validated_data.get('type'),
                to_role = to_role,
                from_date = validated_data.get('from_date'),
                to_date = validated_data.get('to_date'),
                voice = validated_data.get('voice'),
                image = validated_data.get('image'),
                video = validated_data.get('video'),
                comment = validated_data.get('comment'),
                file_bool = validated_data.get('file_bool'),
            )
            
            imams = imams.filter(region__in=region_list)
            if imam_list != []:
                imams.filter(username__in=imam_list)
            if district_list != []:
                imams.filter(district__in=district_list)
            else:
                district_list = Districts.objects.filter(region__in=region_list)
            for i in imams:
                models.DirectionsEmployeeRead.objects.create(
                        direction = direction,
                        employee = i,
                    )
            for i in imams:
                    direction.to_imams.add(i)
            for i in region_list:
                direction.to_region.add(Regions.objects.get(name=i))
            for i in district_list:
                direction.to_district.add(Districts.objects.get(name=i))
            direction.save()
            return direction
        except:
            raise ValidationError('Something went wrong')