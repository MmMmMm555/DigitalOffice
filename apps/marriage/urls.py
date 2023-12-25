from django.urls import path

from apps.marriage.api_endpoints.marriage_crud import views


urlpatterns = [
    # family conflict apis
    path('create/', views.MarriageCreateAPIView.as_view(),
         name='family_conflict_create'),
    path('list/', views.MarriageListAPIView.as_view(),
         name='family_conflict_list'),
    path('detail/<int:pk>/', views.MarriageDetailAPIView.as_view(),
         name='family_conflict_detail'),
    path('update/<int:pk>/', views.MarriageUpdateAPIView.as_view(),
         name='family_conflict_update'),
    path('delete/<int:pk>', views.MarriageDeleteAPIView.as_view(),
         name='family_conflict_delete'),
]
