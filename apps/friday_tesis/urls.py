from django.urls import path
from apps.friday_tesis.api_endpoints.tesis.views import (FridayThesisCreateView,
                                                         FridayThesisListView,
                                                         FridayThesisUpdateView,
                                                         FridayThesisDetailView)
from apps.friday_tesis.api_endpoints.seen_api.views import (FridayThesisImamReadView,
                                                            FridayThesisImamReadListView)
from apps.friday_tesis.api_endpoints.results_api.views import (FridayThesisImamResultView,
                                                               FridayThesisResultDetailView,
                                                               FridayThesisResultUpdateView,
                                                               ResultVideoView,
                                                               ResultImageView,
                                                               ResultImageListView,
                                                               ResultVideoListView,)

urlpatterns = [
    # tesis apis
    path('create/', FridayThesisCreateView.as_view(), name='tesis_create'),
    path('update/<int:pk>/', FridayThesisUpdateView.as_view(), name='tesis_update'),
    path('detail/<int:pk>/', FridayThesisDetailView.as_view(), name='tesis_detail'),
    path('list/', FridayThesisListView.as_view(), name='tesis_list'),

    # seen apis
    path('seen/update/<int:pk>', FridayThesisImamReadView.as_view(),
         name='tesis_seen_update'),
    path('seen/list', FridayThesisImamReadListView.as_view(),
         name='tesis_seen_list'),

    # result apis
    path('result/create', FridayThesisImamResultView.as_view(), name='result_create'),
    path('result/detail/<int:pk>',
         FridayThesisResultDetailView.as_view(), name='result_detail'),
    path('result/update/<int:pk>',
         FridayThesisResultUpdateView.as_view(), name='result_update'),

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
