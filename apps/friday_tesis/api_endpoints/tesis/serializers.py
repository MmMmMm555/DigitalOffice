from rest_framework.serializers import ModelSerializer, ValidationError
from apps.friday_tesis import models
from apps.users.models import User
from apps.common.regions import Regions, Districts


class FridayTesisSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesis
        fields = ('id',
                  'title',
                  'file',
                  'attachment',
                  'to_region',
                  'to_district',
                  'to_imams',
                  'date',
                  'created_at',
                  'updated_at',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['seen_count'] = models.FridayTesisImamRead.objects.filter(tesis=instance, seen=True).count()
        representation['unseen_count'] = models.FridayTesisImamRead.objects.filter(tesis=instance, seen=False).count()
        return representation


class FridayTesisCreateSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesis
        fields = ('id',
                  'title',
                  'file',
                  'attachment',
                  'to_region',
                  'to_district',
                  'to_imams',
                  'date',
                  'created_at',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )

    def create(self, validated_data):
        try:
            tesis = models.FridayTesis.objects.create(
                title = validated_data.get('title'),
                file = validated_data.get('file'),
                attachment = validated_data.get('attachment'),
                date = validated_data.get('date'),
                image = validated_data.get('image'),
                video = validated_data.get('video'),
                comment = validated_data.get('comment'),
                file_bool = validated_data.get('file_bool'),
            )
            imams = User.objects.filter(role='4')
            imam_list = validated_data.get('to_imams', None)
            district_list = validated_data.get('to_district', None)
            region_list = validated_data.get('to_region', None)
            imams = imams.filter(region__in=region_list)
            if imam_list != []:
                imams.filter(username__in=imam_list)
            if district_list != []:
                imams.filter(district__in=district_list)
            else:
                district_list = Districts.objects.filter(region__in=region_list)
            for i in imams:
                models.FridayTesisImamRead.objects.create(
                        tesis = tesis,
                        imam = i,
                    )
            for i in imams:
                    tesis.to_imams.add(i)
            for i in region_list:
                tesis.to_region.add(Regions.objects.get(name=i))
            for i in district_list:
                tesis.to_district.add(Districts.objects.get(name=i))
            tesis.save()
            return tesis
        except:
            raise ValidationError('Something went wrong')