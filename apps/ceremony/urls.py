from django.urls import path

from apps.ceremony.api_endpoints.ceremony_crud import views


urlpatterns = [
    # ceremony apis
    path('create', views.CeremonyCreateAPIView.as_view(),
         name='ceremony_create'),
    path('list/', views.CeremonyListAPIView.as_view(),
         name='ceremony_list'),
    path('detail/<int:pk>', views.CeremonyDetailAPIView.as_view(),
         name='ceremony_detail'),
    path('update/<int:pk>', views.CeremonyUpdateAPIView.as_view(),
         name='ceremony_update'),
    path('delete/<int:pk>', views.CeremonyDeleteAPIView.as_view(),
         name='ceremony_delete'),
]
