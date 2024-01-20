from rest_framework.serializers import ModelSerializer

from apps.users.models import User
from apps.employee.api_endpoints.employee.serializers import EmployeeDetailSerializer


class UserSelfSerializer(ModelSerializer):
    profil = EmployeeDetailSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'role',
                  'email', 'profil', 'region', 'district',)
