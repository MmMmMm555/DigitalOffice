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


class MosqueSingleSerializer(ModelSerializer):
    fire_images = FireDefenseImageSerializer(many=True)
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

    # def to_representation(self, instance):
    #         representation = self.to_representation(instance)
    #         images_id = instance.fire_images
    #         print(images_id)
    #         images = FireDefenseImages.objects.filter(id__in=images_id)
    #         representation['evacuation_road_image'] = images.filter(type='1')
    #         representation['fire_safe_image'] = images.filter(type='2')
    #         representation['fire_closet_image'] = images.filter(type='3')
    #         representation['fire_signal_image'] = images.filter(type='4')
    #         representation['auto_fire_extinguisher_image'] = images.filter(type='5')
    #         return representation


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