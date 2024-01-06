from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticated

from apps.mosque.api_endpoints.Mosque.serializers import (MosqueSerializer,
                                                          MosqueListSerializer,
                                                          MosqueSingleSerializer,
                                                          MosqueUpdateSerializer,)
from apps.mosque.models import Mosque
from apps.common.permissions import IsSuperAdmin, IsRegionAdmin, IsDistrictAdmin


class MosqueCreateView(generics.CreateAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)


class MosqueUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueUpdateSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsSuperAdmin | IsRegionAdmin | IsDistrictAdmin,)


class MosqueListView(generics.ListAPIView):
    """Agar imomi yo'q masjidlar listi kerak bolsa "api/v1/mosque/list/?has_imam=false" qilib filter jo'natiladi"""
    queryset = Mosque.objects.all().annotate(employee_count=Count(
        'employee', filter=Q(employee__profile__role__in=['4', '5'])), has_imam=Count('employee', filter=Q(employee__profile__role='4')))
    serializer_class = MosqueListSerializer
    permission_classes = (IsSuperAdmin,)
    search_fields = ('name', 'address',)
    filterset_fields = (
        'id',
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
        'service_rooms_bool',
        'imam_room',
        'sub_imam_room',
        'casher_room',
        'guard_room',
        'other_room',
        'mosque_library',
        'shrine',
        'graveyard',
        'shop',)

    def get_queryset(self):
        has_imam = self.request.GET.get('has_imam', None)
        if has_imam:
            return self.queryset.filter(has_imam=0)
        return self.queryset


class MosqueRetrieveView(generics.RetrieveAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSingleSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'


class MosqueDeleteView(generics.DestroyAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSerializer
    permission_classes = (IsSuperAdmin,)
    lookup_field = 'pk'
