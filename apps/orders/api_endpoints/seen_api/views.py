from rest_framework import generics, filters, parsers
# from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DirectionsEmployeeReadSerializer, DirectionsEmployeeReadListSerializer
# DirectionsUnseenCount
from apps.orders import models
from apps.common.permissions import IsSuperAdmin, IsImam
from apps.users.models import Role
from django.db.models import F


class DirectionEmployeeReadView(generics.UpdateAPIView):
    queryset = models.DirectionsEmployeeRead.objects.all()
    serializer_class = DirectionsEmployeeReadSerializer
    permission_classes = (IsImam,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class DirectionEmployeeReadListView(generics.ListAPIView):
    queryset = models.DirectionsEmployeeRead.objects.all().annotate(
        mosque=F('employee__profil__mosque__name'), region=F('employee__region__name'), district=F('employee__district__name'), employee_name=F('employee__profil__name'), employee_last_name=F('employee__profil__last_name'))
    serializer_class = DirectionsEmployeeReadListSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('employee__profil_name', 'direction__title',)
    filterset_fields = ('direction', 'direction__direction_type',
                        'created_at', 'state', 'requirement', 'employee', 'employee__profil__mosque', 'employee__region', 'employee__district',)

    def get_queryset(self):
        if self.request.user.role == Role.SUPER_ADMIN:
            return self.queryset
        return self.queryset.filter(employee=self.request.user)


# @api_view(['GET'])
# def UnseenCount(request):
#     models.DirectionsEmployeeRead.objects.filter(
#         state='1', employee=request.user)
#     response = {}
#     x = [{'DECISION': '1'},
#          {'ORDER': '2'},
#          {'PROGRAM': '3'},
#          {'MESSAGE': '4'},
#          {'MISSION': '5'}]
#     for i in range(0, 5):
#         response[x[i].keys()] = {'type': i, 'count': models.DirectionsEmployeeRead.objects.filter(
#             state=str(i), employee=request.user).count()}
#     print(response)
#     return Response(data={'ss': 0}, status=status.HTTP_200_OK)
