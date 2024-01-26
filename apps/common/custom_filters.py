import django_filters
from django.utils import timezone
from apps.public_prayers.models import PublicPrayers
from apps.orders.models import Directions


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


class DirectionFilterSet(django_filters.FilterSet):
    created_at = CreatedAtDateFilter()

    class Meta:
        model = Directions
        fields = ('id', 'created_at', 'to_region', 'to_district', 'required_to_region',
                        'required_to_district', 'from_role', 'types', 'direction_type', 'from_date', 'to_date',)