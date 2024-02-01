from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/common/', include('apps.common.urls')),
    path('api/v2/auth/', include('apps.users.urls')),
    path('api/v2/mosque/', include('apps.mosque.urls')),
    path('api/v2/employee/', include('apps.employee.urls')),
    path('api/v2/thesis/', include('apps.friday_tesis.urls')),
    path('api/v2/direction/', include('apps.orders.urls')),
    path('api/v2/wedding/', include('apps.wedding.urls')),
    path('api/v2/death/', include('apps.death.urls')),
    path('api/v2/marriage/', include('apps.marriage.urls')),
    path('api/v2/mavlud/', include('apps.mavlud.urls')),
    path('api/v2/neighborhood/', include('apps.neighborhood.urls')),
    path('api/v2/individual_conversations/',
         include('apps.individual_conversations.urls')),
    path('api/v2/religious_advice/', include('apps.religious_advice.urls')),
    path('api/v2/public_events/', include('apps.community_events.urls')),
    path('api/v2/scientific_activity/', include('apps.scientific_activity.urls')),
    path('api/v2/charity/', include('apps.charity.urls')),
    path('api/v2/charity_promotion/', include('apps.charity_promotion.urls')),
    path('api/v2/public_prayers/', include('apps.public_prayers.urls')),
    path('api/v2/organizations/', include('apps.organizations.urls')),
    path('api/v2/family_conflicts/', include('apps.family_conflicts.urls')),
    path('api/v2/ceremony/', include('apps.ceremony.urls')),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
