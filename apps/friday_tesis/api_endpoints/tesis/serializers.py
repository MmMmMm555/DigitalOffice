from rest_framework.serializers import ModelSerializer
from apps.friday_tesis import models
from apps.users.models import User
from apps.common.regions import Regions, Districts


class FridayTesisImamReadSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('id', 'tesis', 'to_region', 'to_district', 'to_imams', 'empty', 'image', 'video', 'comment', 'file',)

class FridayTesisSerializer(ModelSerializer):
    # requiredfields = FridayTesisImamReadSerializer
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
                  'empty',
                  'image',
                  'video',
                  'comment',
                  'file_bool',
                  )
   
    def create(self, validated_data):
        print('xxxxxxxxxxxxxxxxxx', validated_data.get('to_imams', None))
        print('xxxxxxxxxxxxxxxxxx', validated_data.get('to_region'))
        print('xxxxxxxxxxxxxxxxxx', validated_data.get('to_district'))
        tesis = models.FridayTesis.objects.create(
            title = validated_data.get('title'),
            file = validated_data.get('file'),
            attachment = validated_data.get('attachment'),
            date = validated_data.get('date'),
            empty = validated_data.get('empty'),
            image = validated_data.get('image'),
            video = validated_data.get('video'),
            comment = validated_data.get('comment'),
            file_bool = validated_data.get('file_bool'),
        )
        imams = User.objects.filter(role='4')
        print(imams)
        imam_list = validated_data.get('to_imams', None)
        district_list = validated_data.get('to_district', None)
        region_list = validated_data.get('to_region', None)
        imams = imams.filter(region__in=region_list)
        print('regionsf' , imams)
        if imam_list != []:
            imams.filter(username__in=imam_list)
        elif district_list != []:
            imams.filter(district__in=district_list)
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
    
# {'title': 'test 2', 'file': <InMemoryUploadedFile: Coursera BED97Q6KDJKA.pdf (application/pdf)>, 'to_region': [<Regions: xorazm>], 'to_district': [<Districts: gurlan>], 'to_imams': [], 'date': datetime.date(2023, 12, 19), 'requiredfields': []}