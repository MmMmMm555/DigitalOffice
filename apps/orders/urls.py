from django.urls import path
from apps.orders.api_endpoints.order.views import (DirectionCreateView,
                                                   DirectionsListView,
                                                   DirectionDeleteView,
                                                   DirectionSingleView,
                                                   DirectionUpdateView,)
from apps.orders.api_endpoints.seen_api.views import DirectionEmployeeReadListView, DirectionEmployeeReadView
from apps.orders.api_endpoints.result_api.views import (DirectionsEmployeeResultView,
                                                               DirectionsEmployeeResultListView,
                                                               ResultVideoView,
                                                               ResultImageView,
                                                               ResultImageListView,
                                                               ResultFileListView,
                                                               ResultFileView,
                                                               ResultVideoListView,)

urlpatterns = [
    # direction apis
    path('create/', DirectionCreateView.as_view(), name='direction_create'),
    path('list/', DirectionsListView.as_view(), name='direction_list'),
    path('update/<int:pk>', DirectionUpdateView.as_view(), name='direction_update'),
    path('delete/<int:pk>', DirectionDeleteView.as_view(), name='direction_delete'),
    path('detail/<int:pk>', DirectionSingleView.as_view(), name='direction_detail'),

    # seen apis
    path('seen/update/<int:pk>', DirectionEmployeeReadView.as_view(), name='order_seen_update'),
    path('seen/list', DirectionEmployeeReadListView.as_view(), name='order_seen_list'),

    # result apis
    path('result/create', DirectionsEmployeeResultView.as_view(), name='result_create'),
    path('result/list', DirectionsEmployeeResultListView.as_view(), name='result_list'),

    # result image vs videos api
    path('result/image/create', ResultImageView.as_view(), name='result_image_create'),
    path('result/video/create', ResultVideoView.as_view(), name='result_video_create'),
    path('result/image/list', ResultImageListView.as_view(), name='result_image_list'),
    path('result/video/list', ResultVideoListView.as_view(), name='result_video_list'),
    path('result/file/create', ResultFileView.as_view(), name='result_file_list'),
    path('result/file/list', ResultFileListView.as_view(), name='result_file_list'),
]
