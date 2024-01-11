from django.urls import path
from apps.common.api_endpoints.regions.views import RegionListView
from apps.common.api_endpoints.districts.views import DistrictListView
from apps.common.api_endpoints.notifications.views import NotificationApi
from apps.common.api_endpoints.statistics.views import (StatisticDirectionTypeApi,
                                                        StatisticRegionApi,
                                                        StatisticStateApi,
                                                        StatisticRoleApi,
                                                        StatisticThesisStateApi,
                                                        StatisticThesisAgeApi,
                                                        StatisticMosqueTopApi,
                                                        StatisticMosqueTypeApi,
                                                        StatisticMosqueStatusApi,
                                                        StatisticMosqueRegionApi,
                                                        )

urlpatterns = [
    # regions api
    path('regions/', RegionListView.as_view(), name='regions_list'),
    path('districts/', DistrictListView.as_view(), name='districts_list'),

    # notifications api
    path('notifications/', NotificationApi, name='districts_list'),

    # statistics order api
    path('statistics/order/direction_type',
         StatisticDirectionTypeApi, name='statistics_direction_type'),
    path('statistics/order/region', StatisticRegionApi, name='statistics_region'),
    path('statistics/order/state', StatisticStateApi, name='statistics_state'),
    path('statistics/order/role', StatisticRoleApi, name='statistics_role'),

    # statistics tesis api
    path('statistics/thesis/state',
         StatisticThesisStateApi, name='statistics_thesis_state'),
    path('statistics/thesis/age', StatisticThesisAgeApi,
         name='statistics_thesis_role'),

    # statistics thesis api
    path('statistics/mosque/top',
         StatisticMosqueTopApi, name='statistics_mosque_top'),
    path('statistics/mosque/type',
         StatisticMosqueTypeApi, name='statistics_mosque_type'),
    path('statistics/mosque/status',
         StatisticMosqueStatusApi, name='statistics_mosque_status'),
    path('statistics/mosque/region',
         StatisticMosqueRegionApi, name='statistics_mosque_region'),
]
