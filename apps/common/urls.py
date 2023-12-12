from django.urls import path
from apps.common.api_endpoints.regions import views 

urlpatterns = [
    path('regions/', views.RegionListView.as_view(), name='regions_list'),
]
