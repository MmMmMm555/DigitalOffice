from rest_framework.serializers import ModelSerializer

from apps.employee.models import Department, Position


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name',)


class DepartmentSerializer(ModelSerializer):
    position = PositionSerializer(many=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'position',)
