from django.urls import path
from apps.orders.api_endpoints.order.views import (DirectionCreateView,
                                                   DirectionsListView,
                                                   DirectionDeleteView,
                                                   DirectionSingleView,
                                                   DirectionUpdateView,)
# from apps.orders.api_endpoints.seen_api.views import DirectionsEmployeeReadListView, DirectionsEmployeeReadView

urlpatterns = [
    # direction apis
    path('create/', DirectionCreateView.as_view(), name='direction_create'),
    path('list/', DirectionsListView.as_view(), name='direction_list'),
    path('update/<int:pk>', DirectionUpdateView.as_view(), name='direction_update'),
    path('delete/<int:pk>', DirectionDeleteView.as_view(), name='direction_delete'),
    path('detail/<int:pk>', DirectionSingleView.as_view(), name='direction_detail'),

#     # seen apis
#     path('seen/', DirectionsEmployeeReadView.as_view(), name='tesis_seen'),
#     path('seen_list/', DirectionsEmployeeReadListView.as_view(), name='tesis_seen_list'),
]