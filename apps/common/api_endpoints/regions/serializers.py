from rest_framework.serializers import ModelSerializer

from apps.common.regions import Regions, Districts


class DistrictsSerializer(ModelSerializer):
    class Meta:
        model = Districts
        fields = ('id', 'name',)

class RegionsSerializer(ModelSerializer):
    district = DistrictsSerializer
    class Meta:
        model = Regions
        fields = ('id', 'name', 'district',)
        depth = 1