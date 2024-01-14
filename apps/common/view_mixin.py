from django.conf import settings
from django.core.cache import cache
from django.db.models import F
from apps.users.models import Role


class ViewCountMixin:
    """Work only with retrieve views"""

    view_count_field = "view_count"

    def _count_view(self):
        instance = self.get_object()
        prefix = "view_count"
        model_name = instance.__class__.__name__
        key = f"{prefix}:{model_name}:{instance.pk}:{self.request.fingerprint}"
        data = cache.get(key)
        if not data:
            setattr(instance, self.view_count_field,
                    F(self.view_count_field) + 1)
            instance.save(update_fields=[self.view_count_field])
            cache.set(key, True, settings.VIEW_COUNT_MIN_VIEW_PERIOD)

    def get(self, request, *args, **kwargs):
        self._count_view()
        return super().get(request, *args, **kwargs)


class FilerQueryByRole:

    def get_queryset(self):
        query = self.queryset
        user_role = self.request.user.role
        if user_role in [Role.IMAM, Role.SUB_IMAM]:
            query = query.filter(imam=self.request.user)
        elif user_role == Role.REGION_ADMIN:
            query = query.filter(imam__region=self.request.user.region)
        elif user_role == Role.DISTRICT_ADMIN:
            query = query.filter(imam__district=self.request.user.district)
        return query
