from rest_framework.serializers import ModelSerializer

from apps.users.models import User
from apps.employee.api_endpoints.employee.serializers import EmployeeDetailSerializer


class UserSelfSerializer(ModelSerializer):
    profil = EmployeeDetailSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'role',
                  'email', 'profil', 'region', 'district',)

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     mosque = None
    #     region = Regions.objects.filter(id=instance.region.id).only('id', 'name').last()
    #     district = Districts.objects.filter(id=instance.district.id).only('id', 'name').last()
    #     if instance.profil:
    #         profile = Employee.objects.filter(id=instance.profil.id).last()
    #         representation['name'] = profile.name
    #         representation['last_name'] = profile.last_name
    #         representation['surname'] = profile.surname
    #         representation['phone'] = str(profile.phone_number)
    #         mosque = Mosque.objects.filter(id=profile.mosque.id).only('id', 'name').last()
    #     if mosque:
    #         representation['mosque'] = mosque.name
    #     if district:
    #         representation['district'] = district.name
    #     if region:
    #         representation['region'] = region.name
    #     return representation
