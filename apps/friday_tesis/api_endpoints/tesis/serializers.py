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
                  'types',
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
        # try:
            tesis = models.FridayTesis.objects.create(
                title = validated_data.get('title', None),
                types = validated_data.get('types', None),
                file = validated_data.get('file', None),
                attachment = validated_data.get('attachment', None),
                date = validated_data.get('date', None),
                image = validated_data.get('image', None),
                video = validated_data.get('video', None),
                comment = validated_data.get('comment', None),
                file_bool = validated_data.get('file_bool', None),
            )
            imams = User.objects.filter(role='4')
            for i in imams:
                models.FridayTesisImamRead.objects.create(
                        tesis = tesis,
                        imam = i,
                    )
            imam_list = validated_data.get('to_imams', [])
            district_list = validated_data.get('to_district', [])
            region_list = validated_data.get('to_region', [])
            imams = imams.filter(region__in=region_list)
            region_list = Regions.objects.filter(name__in=region_list)
            if not district_list:
                district_list = Districts.objects.filter(region__in=region_list)
            if district_list:
                imams = imams.filter(district__in=district_list)
            if imam_list:
                imams = imams.filter(username__in=imam_list)
            for i in imams:
                seen = models.FridayTesisImamRead.objects.filter(
                        tesis = tesis,
                        imam = i,
                    )
                for j in seen:
                    j.requirement = True
                    j.save()
        
            tesis.to_imams.set(imams)
            tesis.to_region.set(region_list)
            tesis.to_district.set(district_list)
            tesis.save()
            return tesis
        # except:
            # raise ValidationError('Something went wrong')