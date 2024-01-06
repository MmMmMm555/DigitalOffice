from django.urls import path

from apps.organizations.api_endpoints.organizations_crud import views


urlpatterns = [
    # organization apis
    path('create/', views.OrganizationCreateAPIView.as_view(),
         name='organization_create'),
    path('list/', views.OrganizationListAPIView.as_view(),
         name='organization_list'),
    path('detail/<int:pk>/', views.OrganizationDetailAPIView.as_view(),
         name='organization_detail'),
    path('update/<int:pk>/', views.OrganizationUpdateAPIView.as_view(),
         name='organization_update'),
    path('delete/<int:pk>', views.OrganizationDeleteAPIView.as_view(),
         name='organization_delete'),
]
