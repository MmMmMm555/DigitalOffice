from django.urls import path

from apps.wedding.api_endpoints.wedding import views


urlpatterns = [
    # wedding apis
    path('create/', views.WeddingCreateAPIView.as_view(),
         name='wedding_create'),
    path('list/', views.WeddingListAPIView.as_view(),
         name='wedding_list'),
    path('detail/<int:pk>/', views.WeddingDetailAPIView.as_view(),
         name='wedding_detail'),
    path('update/<int:pk>/', views.WeddingUpdateAPIView.as_view(),
         name='wedding_update'),
    path('delete/<int:pk>', views.WeddingDeleteAPIView.as_view(),
         name='wedding_delete'),
]
