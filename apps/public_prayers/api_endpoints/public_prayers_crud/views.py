from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
import django_filters
from django.utils import timezone

from apps.common.permissions import IsImam, IsDeputy
from apps.public_prayers.models import PublicPrayers
from apps.users.models import Role
from .serializers import (PublicPrayersSerializer, PublicPrayersListSerializer,
                          PublicPrayersUpdateSerializer, PublicPrayersDetailSerializer,)
from apps.common.view_mixin import FilerQueryByRole


class CreatedAtDateFilter(django_filters.DateFilter):
    def filter(self, queryset, value):
        if value:
            # Assuming your `created_at` field is in UTC
            value = timezone.datetime.combine(
                value, timezone.datetime.min.time(), tzinfo=timezone.utc)
            return queryset.filter(created_at__gte=value, created_at__lt=value + timezone.timedelta(days=1))
        return queryset


class PublicPrayersFilterSet(django_filters.FilterSet):
    created_at = CreatedAtDateFilter()

    class Meta:
        model = PublicPrayers
        fields = ['id', 'imam', 'prayer', 'created_at']


class PublicPrayersCreateAPIView(CreateAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(imam=self.request.user)


class PublicPrayersListAPIView(FilerQueryByRole, ListAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersListSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ('title',)
    filterset_class = PublicPrayersFilterSet


class PublicPrayersDetailAPIView(RetrieveAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersDetailSerializer
    permission_classes = (IsAuthenticated,)


class PublicPrayersUpdateAPIView(UpdateAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersUpdateSerializer
    permission_classes = (IsImam | IsDeputy,)
    parser_classes = (MultiPartParser, FormParser,)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.imam == self.request.user:
            serializer.save(imam=self.request.user)
        else:
            return Response({'message': 'You are not allowed to update'}, status=403)


class PublicPrayersDeleteAPIView(DestroyAPIView):
    queryset = PublicPrayers.objects.all()
    serializer_class = PublicPrayersSerializer
    permission_classes = (IsImam | IsDeputy,)

    def perform_destroy(self, instance):
        if instance.imam == self.request.user:
            instance.delete()
        else:
            return Response({'message': 'You are not allowed to delete'}, status=403)
