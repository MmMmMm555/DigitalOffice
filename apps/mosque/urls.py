from django.urls import path

from apps.mosque.api_endpoints.Mosque.views import (MosqueCreateView,
                                                    MosqueListView, 
                                                    MosqueRetrieveView,
                                                    MosqueUpdateView,)
from apps.mosque.api_endpoints.FireImages.views import (FireDefenseImagesCreateView,
                                                        FireDefenseImagesRetrieveView)


urlpatterns = [
    # mosque api
    path('create/', MosqueCreateView.as_view(), name='mosque_create'),
    path('list/', MosqueListView.as_view(), name='mosque_list'),
    path('update/<int:pk>', MosqueUpdateView.as_view(), name='mosque_update'),
    path('single/<int:pk>', MosqueRetrieveView.as_view(), name='mosque_single'),
    
    # fire defense images api
    path('fire_image/create', FireDefenseImagesCreateView.as_view(), name='fire_image_create'),
    path('fire_image/single/<int:pk>', FireDefenseImagesRetrieveView.as_view(), name='fire_image_single'),
]