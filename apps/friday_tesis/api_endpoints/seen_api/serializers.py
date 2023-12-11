from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.response import Response
from apps.friday_tesis import models
# from apps.users.models import User
# from apps.common.regions import Regions, Districts


class FridayTesisImamReadSerializer(ModelSerializer):
    class Meta:
        model = models.FridayTesisImamRead
        fields = ('tesis',)
    
    def create(self, validatet_data):
        tesis = validatet_data.get('tesis', None)
        imam = self.context.get('request').user
        try:
            read = models.FridayTesisImamRead.objects.filter(imam=imam, tesis=tesis).first()
            if read:
                read.seen = True
                read.save()
                return read
            raise ValidationError('query not found')
        except:
            raise ValidationError('something went wrogn')