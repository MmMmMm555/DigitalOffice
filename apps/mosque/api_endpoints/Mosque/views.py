from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser

from apps.mosque.api_endpoints.Mosque.serializers import (MosqueSerializer,
                                                          MosqueListSerializer,
                                                          MosqueSingleSerializer,
                                                          MosqueUpdateSerializer,)
from apps.mosque.models import Mosque
from apps.common.permissions import IsSuperAdmin, IsImam


class MosqueCreateView(generics.CreateAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsSuperAdmin,)


class MosqueUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueUpdateSerializer
    parser_classes = (FormParser, MultiPartParser,)
    permission_classes = (IsSuperAdmin,)


class MosqueListView(generics.ListAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueListSerializer
    permission_classes = (IsSuperAdmin,)
    search_fields = ('name', 'address',)
    filterset_fields = (
                       'id',
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
    
    def get_queryset(self):
        if self.request.user.role == '1':
            return Mosque.objects.all()
        id = self.request.user.profil.mosque
        return self.queryset.filter(id=id)

class MosqueRetrieveView(generics.RetrieveAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSingleSerializer
    permission_classes = (IsSuperAdmin | IsImam,)
    lookup_field = 'pk'

    def get_queryset(self):
        if self.request.user.role == '1':
            return Mosque.objects.all()
        id = self.request.user.profil.mosque
        return self.queryset.filter(id=id)