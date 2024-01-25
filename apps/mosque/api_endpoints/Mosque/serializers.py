from rest_framework.serializers import (
    ModelSerializer, IntegerField,)

from apps.mosque.models import Mosque, FireDefenseImages
from apps.common.api_endpoints.districts.serializers import RegionsSerializer
from apps.common.api_endpoints.regions.serializers import DistrictsSerializer
from apps.common.related_serializers import EmployeeRelatedSerializer


class FireDefenseImageSerializer(ModelSerializer):
    class Meta:
        model = FireDefenseImages
        fields = ('id', 'image', 'type',)


class MosqueSerializer(ModelSerializer):
    class Meta:
        model = Mosque
        fields = [
            'id',
            'name',
            'address',
            'region',
            'district',
            'location',
            'image',

            'built_at',
            'registered_at',

            'parking',
            'parking_capacity',

            'basement',
            'second_floor',
            'third_floor',
            'capacity',
            'cultural_heritage',

            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'emergency_exit_door',
            'evacuation_road',
            'fire_images',

            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'other_room_amount',

            'mosque_library',
            'shrine',
            'graveyard',
            'shop',

            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
        ]


class MosqueChoiceListSerializer(MosqueSerializer):
    has_imam = IntegerField(read_only=True)
    region = RegionsSerializer(many=False, read_only=True,)
    district = DistrictsSerializer(many=False, read_only=True,)

    class Meta:
        model = Mosque
        fields = (
            'id',
            'name',
            'has_imam',
            'address',
            'region',
            'district',)
        read_only_fields = fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['has_imam'] = False
        if instance.has_imam >= 1:
            representation['has_imam'] = True
        return representation


class MosqueListSerializer(MosqueSerializer):
    # employee_count = IntegerField(read_only=True)
    has_imam = IntegerField(read_only=True)
    region = RegionsSerializer(many=False, read_only=True,)
    district = DistrictsSerializer(many=False, read_only=True,)

    class Meta:
        model = Mosque
        fields = (
            'id',
            'name',
            'address',
            # 'employee_count',
            'has_imam',
            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
            'region',
            'district',
            'built_at',
            # 'registered_at',
            'parking',
            # 'basement',
            'capacity',
            # 'second_floor',
            # 'third_floor',
            # 'cultural_heritage',
            # 'fire_safety',
            # 'auto_fire_extinguisher',
            # 'fire_closet',
            # 'fire_signal',
            # 'emergency_exit_door',
            # 'evacuation_road',
            # 'service_rooms_bool',
            # 'imam_room',
            # 'sub_imam_room',
            # 'casher_room',
            # 'guard_room',
            # 'other_room',
            # 'mosque_library',
            # 'shrine',
            # 'graveyard',
            # 'shop',
            )
        read_only_fields = fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['has_imam'] = False
        if instance.has_imam >= 1:
            representation['has_imam'] = True
        return representation


class MosqueSingleSerializer(ModelSerializer):
    region = RegionsSerializer(many=False, read_only=True,)
    district = DistrictsSerializer(many=False, read_only=True,)
    employee = EmployeeRelatedSerializer(many=True, read_only=True,)

    class Meta:
        model = Mosque
        fields = (
            'id',
            'name',
            'address',
            'region',
            'district',
            'location',
            'image',

            'built_at',
            'registered_at',

            'parking',
            'parking_capacity',

            'basement',
            'second_floor',
            'third_floor',
            'capacity',
            'cultural_heritage',

            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'emergency_exit_door',
            'evacuation_road',
            'fire_images',

            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'other_room_amount',

            'mosque_library',
            'shrine',
            'graveyard',
            'shop',

            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
            'created_at',
            'updated_at',

            'employee',)
        read_only_fields = fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        images = instance.fire_images.all()
        representation['evacuation_road_image'] = FireDefenseImageSerializer(
            images.filter(type='1'), many=True, context=self.context).data
        representation['fire_safe_image'] = FireDefenseImageSerializer(
            images.filter(type='2'), many=True, context=self.context).data
        representation['fire_closet_image'] = FireDefenseImageSerializer(
            images.filter(type='3'), many=True, context=self.context).data
        representation['fire_signal_image'] = FireDefenseImageSerializer(
            images.filter(type='4'), many=True, context=self.context).data
        representation['auto_fire_extinguisher_image'] = FireDefenseImageSerializer(
            images.filter(type='5'), many=True, context=self.context).data
        representation['emergency_exit_door_image'] = FireDefenseImageSerializer(
            images.filter(type='6'), many=True, context=self.context).data
        return representation


class MosqueUpdateSerializer(ModelSerializer):

    class Meta:
        model = Mosque
        fields = (
            'id',
            'name',
            'address',
            'region',
            'district',
            'location',
            'image',

            'built_at',
            'registered_at',

            'parking',
            'parking_capacity',

            'basement',
            'second_floor',
            'third_floor',
            'capacity',
            'cultural_heritage',

            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'emergency_exit_door',
            'evacuation_road',
            'fire_images',

            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'other_room_amount',

            'mosque_library',
            'shrine',
            'graveyard',
            'shop',

            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
        )
        extra_kwargs = {
            'name': {'required': False},
            'address': {'required': False},
            'region': {'required': False},
            'district': {'required': False},
            'location': {'required': False},
            'built_at': {'required': False},
            'registered_at': {'required': False},
        }
