from rest_framework.serializers import ModelSerializer
from apps.friday_tesis import models
from apps.users.models import User

class FridayTesisRequiredFieldsSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisReqiredFields
        fields = ('id', 'tesis', 'to_region', 'to_district', 'to_imams', 'empty', 'image', 'video', 'comment', 'file',)

class FridayTesisSerializer(ModelSerializer):
    requiredfields = FridayTesisRequiredFieldsSerializer
    class Meta:
        model = models.FridayTesis
        fields = ('id', 'title', 'file', 'attachment', 'to_region', 'to_district', 'to_imams', 'date', 'requiredfields', 'created_at', 'updated_at',)
        
    # def create(self, validated_data):
    #     print('xxxxxxxxxxxxxxxxxx', validated_data.get('to_imams', None))
    #     print('xxxxxxxxxxxxxxxxxx', validated_data.get('to_region'))
    #     print('xxxxxxxxxxxxxxxxxx', validated_data.get('to_district'))
    #     tesis = models.FridayTesis.objects.create(
    #         title = validated_data.get('title'),
    #         file = validated_data.get('file'),
    #         attachment = validated_data.get('attachment'),
    #         date = validated_data.get('date'),
    #         # requiredfields = validated_data.get('requiredfields'),
    #     )
    #     if validated_data.get('to_imams', None) == []:
    #         for i in User.objects.all().values_list('id', flat=True):
    #             tesis.to_imams.add(i)
    #     else:
    #         pass
    #         # tesis.to_region.add(validated_data.get('to_region'))
    #         # tesis.to_district.add(validated_data.get('to_district'))
    #     # tesis.set(validated_data.get('requiredfields'))
    #     tesis.save()
    #     return tesis
    
# {'title': 'test 2', 'file': <InMemoryUploadedFile: Coursera BED97Q6KDJKA.pdf (application/pdf)>, 'to_region': [<Regions: xorazm>], 'to_district': [<Districts: gurlan>], 'to_imams': [], 'date': datetime.date(2023, 12, 19), 'requiredfields': []}