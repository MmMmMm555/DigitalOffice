from rest_framework.serializers import ModelSerializer

from apps.common.regions import Regions, Districts

class RegionsSerializer(ModelSerializer):
    class Meta:
        model = Regions
        fields = ('id', 'name',)

class DistrictsSerializer(ModelSerializer):
    class Meta:
        model = Districts
        fields = ('id', 'name', 'region',)
        depth = 1

