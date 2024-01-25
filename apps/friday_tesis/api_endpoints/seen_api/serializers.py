from rest_framework.serializers import ModelSerializer, ValidationError, CharField

from apps.friday_tesis import models
from apps.orders.models import States, User

# class EmployeeRelatedSerializer(ModelSerializer):
#     mosque = CharField(source='mosque.name', default=None)
#     class Meta:
#         model = Employee
#         fields = ('first_name', 'last_name', 'mosque',)
#         read_only_fields = fields


class UserSerializer(ModelSerializer):
    first_name = CharField(source='profil.first_name', default=None)
    last_name = CharField(source='profil.last_name', default=None)
    region = CharField(source='region.name', default=None)
    district = CharField(source='district.name', default=None)
    mosque = CharField(source='profil.mosque.name', default=None)

    class Meta:
        model = User
        fields = ('id', 'region', 'district',
                  'first_name', 'mosque', 'last_name',)
        read_only_fields = fields


class FridayThesisImamReadSerializer(ModelSerializer):
    class Meta:
        model = models.FridayThesisImamRead
        fields = ('id',)

    def save(self):
        thesis = self.instance
        imam = self.context.get('request').user
        if thesis.imam == imam:
            if thesis:
                thesis.state = States.ACCEPTED
                thesis.save()
                return thesis
            raise ValidationError('query not found')
        raise ValidationError('you are not allowed to this action')


class FridayThesisImamReadListSerializer(ModelSerializer):
    imam = UserSerializer(many=False, read_only=True,)

    class Meta:
        model = models.FridayThesisImamRead
        fields = ('id', 'tesis', 'imam', 'state', 'requirement', 'created_at',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['result_id'] = None
        if instance.state == States.DONE:
            try:
                result = models.FridayThesisImamResult.objects.filter(
                    imam=instance.imam, tesis=instance.tesis).last().id
            except:
                result = None
            representation['result_id'] = result
        return representation
