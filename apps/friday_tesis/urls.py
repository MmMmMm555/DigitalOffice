from django.urls import path
from apps.friday_tesis.api_endpoints.tesis.views import (FridayTesisCreateView,
                                                         FridayTesisListView,
                                                         FridayTesisUpdateView,
                                                         FridayTesisDetailView)
from apps.friday_tesis.api_endpoints.seen_api.views import (FridayTesisImamReadView,
                                                            FridayTesisImamReadListView)
from apps.friday_tesis.api_endpoints.results_api.views import (FridayTesisImamResultView,
                                                               FridayTesisImamResultListView,
                                                               FridayTesisResultDetailView,
                                                               FridayTesisResultUpdateView,
                                                               ResultVideoView,
                                                               ResultImageView,
                                                               ResultImageListView,
                                                               ResultVideoListView,)

urlpatterns = [
    # tesis apis
    path('create/', FridayTesisCreateView.as_view(), name='tesis_create'),
    path('update/<int:pk>/', FridayTesisUpdateView.as_view(), name='tesis_update'),
    path('detail/<int:pk>/', FridayTesisDetailView.as_view(), name='tesis_detail'),
    path('list/', FridayTesisListView.as_view(), name='tesis_list'),

    # seen apis
    path('seen/update/<int:pk>', FridayTesisImamReadView.as_view(),
         name='tesis_seen_update'),
    path('seen/list', FridayTesisImamReadListView.as_view(),
         name='tesis_seen_list'),

    # result apis
    path('result/create', FridayTesisImamResultView.as_view(), name='result_create'),
    path('result/detail/<int:pk>',
         FridayTesisResultDetailView.as_view(), name='result_detail'),
    path('result/update/<int:pk>',
         FridayTesisResultUpdateView.as_view(), name='result_update'),
    path('result/list', FridayTesisImamResultListView.as_view(), name='result_list'),

    # result image vs videos api
    path('result/image/create', ResultImageView.as_view(),
         name='result_image_create'),
    path('result/video/create', ResultVideoView.as_view(),
         name='result_video_create'),
    path('result/image/list', ResultImageListView.as_view(),
         name='result_image_list'),
    path('result/video/list', ResultVideoListView.as_view(),
         name='result_video_list'),
]
