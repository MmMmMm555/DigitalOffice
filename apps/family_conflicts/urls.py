from django.urls import path

from apps.family_conflicts.api_endpoints.family_conflict_crud import views


urlpatterns = [
    # family conflict apis
    path('create/', views.FamilyConflictCreateAPIView.as_view(),
         name='family_conflict_create'),
    path('list/', views.FamilyConflictListAPIView.as_view(),
         name='family_conflict_list'),
    path('detail/<int:pk>/', views.FamilyConflictDetailAPIView.as_view(),
         name='family_conflict_detail'),
    path('update/<int:pk>/', views.FamilyConflictUpdateAPIView.as_view(),
         name='family_conflict_update'),
    path('delete/<int:pk>', views.FamilyConflictDeleteAPIView.as_view(),
         name='family_conflict_delete'),
]
