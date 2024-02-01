from rest_framework import generics, parsers, permissions

from .serializers import DirectionsEmployeeReadListSerializer, DirectionsEmployeeReadSerializer
from apps.orders import models
from apps.common.permissions import IsImam, IsDistrictAdmin, IsRegionAdmin, IsDeputy, IsDirectionResultOwner
from apps.users.models import Role


class DirectionEmployeeReadView(generics.UpdateAPIView):
    queryset = models.DirectionsEmployeeResult.objects.all()
    serializer_class = DirectionsEmployeeReadSerializer
    permission_classes = ((IsImam | IsDistrictAdmin |
                          IsRegionAdmin | IsDeputy), IsDirectionResultOwner,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class DirectionEmployeeReadListView(generics.ListAPIView):
    queryset = models.DirectionsEmployeeResult.objects.only(
        'id', 'direction', 'employee', 'state', 'requirement', 'created_at', 'updated_at',).select_related(
            'employee', 'employee__profil', 'employee__region', 'employee__district', 'employee__profil__mosque',)
    serializer_class = DirectionsEmployeeReadListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('employee__profil__first_name',
                     'employee__profil__last_name', 'direction__title',)
    filterset_fields = ('direction', 'direction__direction_type', 'state', 'requirement',
                        'employee__profil__mosque', 'employee__region', 'employee__district',)

    def get_queryset(self):
        to_role = self.request.GET.get('to_role')
        user_role = self.request.user.role
        start_date = self.request.GET.get('start_date')
        finish_date = self.request.GET.get('finish_date')
        query = self.queryset
        if user_role == Role.REGION_ADMIN:
            query = query.filter(employee__region=self.request.user.region)
        if user_role in [Role.IMAM, Role.SUB_IMAM,]:
            query = query.filter(employee=self.request.user)
        elif user_role == Role.DISTRICT_ADMIN:
            query = query.filter(employee__district=self.request.user.district)
        if to_role:
            query = query.filter(direction__to_role__contains=[to_role])
        elif start_date:
            query = query.filter(updated_at__gte=start_date)
        elif finish_date:
            query = query.filter(updated_at__lte=finish_date)
        return query
