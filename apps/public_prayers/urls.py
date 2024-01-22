from django.urls import path

from apps.public_prayers.api_endpoints.public_prayers_crud import views
from apps.public_prayers.api_endpoints.prayers_api.views import PrayersListAPIView


urlpatterns = [
    # public prayers apis
    path('create', views.PublicPrayersCreateAPIView.as_view(),
         name='public_prayers_create'),
    path('list/', views.PublicPrayersListAPIView.as_view(),
         name='public_prayers_list'),
    path('detail/<int:pk>', views.PublicPrayersDetailAPIView.as_view(),
         name='public_prayers_detail'),
    path('update/<int:pk>', views.PublicPrayersUpdateAPIView.as_view(),
         name='public_prayers_update'),
    path('delete/<int:pk>', views.PublicPrayersDeleteAPIView.as_view(),
         name='public_prayers_delete'),
    
    # prayer times apis
    path('prayer_times/list/', PrayersListAPIView.as_view(), name='prayer_times_list')
]
