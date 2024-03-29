from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (CharityCreateSerializer, 
                          CharityImageSerializer, 
                          CharityUpdateSerializer,
                          CharityDetailSerializer)
from apps.charity.models import Charity, Images
from apps.common.permissions import IsImam, IsDeputy, IsSuperAdmin
from apps.common.view_mixin import FilerQueryByRole


class CharityCreateView(CreateAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityCreateSerializer
    parser_classes = (FormParser,)
    permission_classes = (IsImam | IsDeputy,)

    def perform_create(self, serializer):
        if self.request.user.role in ['4', '5']:
            serializer.save(imam=self.request.user)
        serializer.save()


class CharityUpdateView(UpdateAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityUpdateSerializer
    parser_classes = (FormParser,)
    permission_classes = (IsImam|IsDeputy,)
    lookup_field = 'pk'


class CharityListView(FilerQueryByRole, ListAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityCreateSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id', 'imam', 'types',
                        'help_type', 'from_who', 'date',)


class CharityImageCreateView(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = CharityImageSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsImam|IsDeputy,)

class CharityImageListView(ListAPIView):
    queryset = Images.objects.all()
    serializer_class = CharityImageSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('id',)  


class CharityDetailView(RetrieveAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityDetailSerializer
    permission_classes = (IsAuthenticated,)

class CharityDeleteView(DestroyAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharityDetailSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)