from django.urls import path

from apps.mosque.api_endpoints.Mosque.views import (MosqueCreateView,
                                                    MosqueListView, 
                                                    MosqueRetrieveView,
                                                    MosqueUpdateView,
                                                    MosqueDeleteView,
                                                    MosqueExcelData,)
from apps.mosque.api_endpoints.FireImages.views import (FireDefenseImagesCreateView,
                                                        FireDefenseImagesRetrieveView,
                                                        FireDefenseImagesListView)


urlpatterns = [
    # mosque api
    path('create/', MosqueCreateView.as_view(), name='mosque_create'),
    path('list/', MosqueListView.as_view(), name='mosque_list'),
    path('excel/', MosqueExcelData.as_view(), name='mosque_excel'),
    path('update/<int:pk>', MosqueUpdateView.as_view(), name='mosque_update'),
    path('detail/<int:pk>', MosqueRetrieveView.as_view(), name='mosque_single'),
    path('delete/<int:pk>', MosqueDeleteView.as_view(), name='mosque_delete'),
    
    # fire defense images api
    path('fire_image/create', FireDefenseImagesCreateView.as_view(), name='fire_image_create'),
    path('fire_image/list', FireDefenseImagesListView.as_view(), name='fire_image_list'),
    path('fire_image/single/<int:pk>', FireDefenseImagesRetrieveView.as_view(), name='fire_image_single'),
]