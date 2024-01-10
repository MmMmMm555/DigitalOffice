from django.urls import path
from apps.common.api_endpoints.regions.views import RegionListView
from apps.common.api_endpoints.districts.views import DistrictListView
from apps.common.api_endpoints.notifications.views import NotificationApi

urlpatterns = [
    # regions api
    path('regions/', RegionListView.as_view(), name='regions_list'),
    path('districts/', DistrictListView.as_view(), name='districts_list'),

    # notifications api
    path('notifications/', NotificationApi, name='districts_list'),
]
