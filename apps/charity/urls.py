from django.urls import path

from apps.charity.api_endpoints.charity import views

urlpatterns = [
    # charity api
    path('create/', views.CharityCreateView.as_view(), name='charity_create'), 
    path('list/', views.CharityListView.as_view(), name='charity_list'), 
    path('update/<int:pk>', views.CharityUpdateView.as_view(), name='charity_update'), 

    # images apis
    path('image/create/', views.CharityImageCreateView.as_view(), name='charity_image_create'),
   
]