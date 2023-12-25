from django.urls import path

from apps.mavlud.api_endpoints.mavlud_crud import views


urlpatterns = [
    # mavlud apis
    path('create/', views.MavludCreateAPIView.as_view(),
         name='mavlud_create'),
    path('list/', views.MavludListAPIView.as_view(),
         name='mavlud_list'),
    path('detail/<int:pk>/', views.MavludDetailAPIView.as_view(),
         name='mavlud_detail'),
    path('update/<int:pk>/', views.MavludUpdateAPIView.as_view(),
         name='mavlud_update'),
    path('delete/<int:pk>', views.MavludDeleteAPIView.as_view(),
         name='mavlud_delete'),
]
