from rest_framework.serializers import ModelSerializer, ImageField

from apps.mosque.models import Mosque, FireDefenseImages


class FireDefenseImageSerializer(ModelSerializer):
    image = ImageField(use_url=True)

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
            'district',
            'location',

            'built_at',
            'registered_at',

            'parking',
            'parking_capacity',

            'basement',
            'second_floor',
            'third_floor',

            'cultural_heritage',

            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'fire_images',

            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'other_room_amount',

            'mosque_library',

            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
        ]


class MosqueListSerializer(MosqueSerializer):
    class Meta:
        model = Mosque
        fields = (
            'id',
            'name',
            'address',
            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
            'district',
            'built_at',
            'registered_at',
            'parking',
            'basement',
            'second_floor',
            'third_floor',
            'cultural_heritage',
            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'mosque_library',)


class MosqueSingleSerializer(ModelSerializer):
    class Meta:
        model = Mosque
        fields = [
            'id',
            'name',
            'address',
            'district',
            'location',

            'built_at',
            'registered_at',

            'parking',
            'parking_capacity',

            'basement',
            'second_floor',
            'third_floor',

            'cultural_heritage',

            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'fire_images',

            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'other_room_amount',

            'mosque_library',

            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
            'created_at',
            'updated_at',
        ]

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

        return representation


class MosqueUpdateSerializer(ModelSerializer):

    class Meta:
        model = Mosque
        fields = (
            'id',
            'name',
            'address',
            'district',
            'location',

            'built_at',
            'registered_at',

            'parking',
            'parking_capacity',

            'basement',
            'second_floor',
            'third_floor',

            'cultural_heritage',

            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'fire_images',

            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'other_room_amount',

            'mosque_library',

            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
        )
        extra_kwargs = {
            'name': {'required': False},
            'address': {'required': False},
            'district': {'required': False},
            'location': {'required': False},
            'built_at': {'required': False},
            'registered_at': {'required': False},
        }
