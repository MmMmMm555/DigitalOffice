from django.urls import path

from apps.marriage.api_endpoints.marriage_crud import views


urlpatterns = [
    # marriage apis
    path('create', views.MarriageCreateAPIView.as_view(),
         name='marriage_create'),
    path('list/', views.MarriageListAPIView.as_view(),
         name='marriage_list'),
    path('detail/<int:pk>', views.MarriageDetailAPIView.as_view(),
         name='marriage_detail'),
    path('update/<int:pk>', views.MarriageUpdateAPIView.as_view(),
         name='marriage_update'),
    path('delete/<int:pk>', views.MarriageDeleteAPIView.as_view(),
         name='marriage_delete'),
]
