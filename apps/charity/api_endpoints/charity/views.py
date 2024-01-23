from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from .serializers import (CharityCreateSerializer,
                          CharityImageSerializer,
                          CharityUpdateSerializer,
                          CharityDetailSerializer,
                          CharityListSerializer,)
from apps.charity.models import Charity, Images
from apps.common.permissions import IsImam, IsDeputy, IsOwner
from apps.common.view_mixin import FilerQueryByRole


class CharityCreateView(CreateAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityCreateSerializer
    parser_classes = (FormParser,)
    permission_classes = (IsImam | IsDeputy,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class CharityUpdateView(UpdateAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityUpdateSerializer
    parser_classes = (FormParser,)
    permission_classes = (IsImam | IsDeputy, IsOwner,)
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        serializer.save(imam=self.request.user)


class CharityListView(FilerQueryByRole, ListAPIView):
    queryset = Charity.objects.only('id', 'imam', 'types', 'date',).select_related('imam', 'imam__profil',)
    serializer_class = CharityListSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'types',
                        'help_type', 'from_who', 'date',)


class CharityImageCreateView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = CharityImageSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsImam | IsDeputy,)


class CharityImageListView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = CharityImageSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id',)


class CharityDetailView(RetrieveAPIView):
    queryset = Charity.objects.all().select_related('imam', 'imam__profil',)
    serializer_class = CharityDetailSerializer
    permission_classes = (IsAuthenticated,)


class CharityDeleteView(DestroyAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityDetailSerializer
    permission_classes = (IsImam | IsDeputy, IsOwner,)
