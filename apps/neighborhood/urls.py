from django.urls import path

from apps.neighborhood.api_endpoints.neighbourhood_crud import views


urlpatterns = [
    # neighborhood apis
    path('create/', views.NeighborhoodCreateAPIView.as_view(),
         name='neighborhood_create'),
    path('list/', views.NeighborhoodListAPIView.as_view(),
         name='neighborhood_list'),
    path('detail/<int:pk>/', views.NeighborhoodDetailAPIView.as_view(),
         name='neighborhood_detail'),
    path('update/<int:pk>/', views.NeighborhoodUpdateAPIView.as_view(),
         name='neighborhood_update'),
    path('delete/<int:pk>', views.NeighborhoodDeleteAPIView.as_view(),
         name='neighborhood_delete'),
]
