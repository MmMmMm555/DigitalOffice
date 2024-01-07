from rest_framework.serializers import ModelSerializer

from apps.employee.models import Graduation


class GraduationSerializer(ModelSerializer):
    class Meta:
        model = Graduation
        fields = ('id', 'name',)
