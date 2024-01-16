import django_filters
from django.utils import timezone
from apps.public_prayers.models import PublicPrayers


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