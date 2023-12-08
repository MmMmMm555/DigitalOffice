from rest_framework import serializers

from apps.mosque.models import Mosque



class MosqueMainSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Mosque
        fields = [
            'name',
            'address',
            'location',
            'built_at',
            'registered_at',
            'mosque_type',
            'mosque_status',
        ]
