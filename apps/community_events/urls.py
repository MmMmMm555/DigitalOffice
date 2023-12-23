from django.urls import path

from apps.community_events.api_endpoints.event_crud.views import (
    CommunityEventsCreateAPIView, CommunityEventListAPIView, 
    CommunityEventsUpdateAPIView, CommunityEventsDetailAPIView, 
    CommunityEventsDeleteAPIView,)
from apps.community_events.api_endpoints.images_api.views import (
    ImageCreateApiView, ImageListApiView,)

urlpatterns = [
    # community events apis
    path('create', CommunityEventsCreateAPIView.as_view(), name='create'),
    path('list', CommunityEventListAPIView.as_view(), name='list'),
    path('update/<int:pk>', CommunityEventsUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>', CommunityEventsDetailAPIView.as_view(), name='detail'),
    path('delete/<int:pk>', CommunityEventsDeleteAPIView.as_view(), name='delete'),

    # images apis
    path('image/create', ImageCreateApiView.as_view(), name='image_create'),
    path('image/list/', ImageListApiView.as_view(), name='image_list'),
]
