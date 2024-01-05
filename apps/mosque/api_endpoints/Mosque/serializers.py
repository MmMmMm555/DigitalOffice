from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.mosque.models import Mosque, FireDefenseImages


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
            'region',
            'district',
            'built_at',
            'registered_at',
            'parking',
            'basement',
            'capacity',
            'second_floor',
            'third_floor',
            'cultural_heritage',
            'fire_safety',
            'auto_fire_extinguisher',
            'fire_closet',
            'fire_signal',
            'emergency_exit_door',
            'evacuation_road',
            'service_rooms_bool',
            'imam_room',
            'sub_imam_room',
            'casher_room',
            'guard_room',
            'other_room',
            'mosque_library',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.region:
            representation['region'] = {'name': instance.region.name,
                                        'id': instance.region.id, }
        if instance.district:
            representation['district'] = {'name': instance.district.name,
                                          'id': instance.district.id, }
        return representation


class MosqueSingleSerializer(ModelSerializer):
    employee = SerializerMethodField()

    class Meta:
        model = Mosque
        fields = [
            'id',
            'name',
            'address',
            'region',
            'district',
            'location',

            'employee',

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

            'mosque_type',
            'mosque_status',
            'mosque_heating_type',
            'mosque_heating_fuel',
            'created_at',
            'updated_at',
        ]

    def get_employee(self, obj):
        return obj.employee.all().values('id', 'name', 'last_name',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        images = instance.fire_images.all().values('id', 'type', 'image',)
        if instance.region:
            representation['region'] = {'name': instance.region.name,
                                        'id': instance.region.id, }
        if instance.district:
            representation['district'] = {'name': instance.district.name,
                                          'id': instance.district.id, }
        representation['evacuation_road_image'] = images.filter(type='1')
        representation['fire_safe_image'] = images.filter(type='2')
        representation['fire_closet_image'] = images.filter(type='3')
        representation['fire_signal_image'] = images.filter(type='4')
        representation['auto_fire_extinguisher_image'] = images.filter(
            type='5')
        representation['emergency_exit_door_image'] = images.filter(type='6')

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
