from django.urls import path
from apps.death.api_endpoints.death_crud import views


urlpatterns = [
    # death apis
    path('create/', views.DeathCreateAPIView.as_view(), name='death_create'),
    path('list/', views.DeathListAPIView.as_view(), name='death_list'),
    path('update/<int:pk>/', views.DeathUpdateAPIView.as_view(), name='death_update'),
    path('detail/<int:pk>/', views.DeathDetailAPIView.as_view(), name='death_detail'),
    path('delete/<int:pk>/', views.DeathDeleteAPIView.as_view(), name='death_delete'),
]
