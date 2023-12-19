from rest_framework.serializers import ModelSerializer

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


class MosqueSingleSerializer(MosqueSerializer):
    fire_images = FireDefenseImageSerializer(many=True)