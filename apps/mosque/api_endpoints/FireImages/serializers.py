from rest_framework import serializers
from apps.mosque.models import FireDefenseImages


class FireDefenseImageSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = FireDefenseImages
        fields = ('id', 'image', 'type', 'created_at', 'updated_at',)
