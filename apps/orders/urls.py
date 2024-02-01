from django.urls import path
from apps.orders.api_endpoints.order.views import (DirectionCreateView,
                                                   DirectionsListView,
                                                   DirectionSingleView,
                                                   DirectionUpdateView,
                                                   FileListView,
                                                   FileView,)
from apps.orders.api_endpoints.seen_api.views import DirectionEmployeeReadListView, DirectionEmployeeReadView

from apps.orders.api_endpoints.result_api.views import (DirectionsEmployeeResultDetailView,
                                                        DirectionsEmployeeResultUpdateView,
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
    path('detail/<int:pk>', DirectionSingleView.as_view(), name='direction_detail'),
    path('file/create', FileView.as_view(), name='file_create'),
    path('file/list', FileListView.as_view(), name='file_list'),

    # seen apis
    path('notification/state/<int:pk>', DirectionEmployeeReadView.as_view(),
         name='order_seen_update'),
    path('notification/list/', DirectionEmployeeReadListView.as_view(),
         name='order_seen_list'),

    # result apis
    path('result/detail/<int:pk>',
         DirectionsEmployeeResultDetailView.as_view(), name='result_detail'),
    path('result/update/<int:pk>',
         DirectionsEmployeeResultUpdateView.as_view(), name='result_update'),

    # result image vs videos api
    path('result/image/create', ResultImageView.as_view(),
         name='result_image_create'),
    path('result/video/create', ResultVideoView.as_view(),
         name='result_video_create'),
    path('result/image/list', ResultImageListView.as_view(),
         name='result_image_list'),
    path('result/video/list', ResultVideoListView.as_view(),
         name='result_video_list'),
    path('result/file/create', ResultFileView.as_view(), name='result_file_create'),
    path('result/file/list', ResultFileListView.as_view(), name='result_file_list'),
]
