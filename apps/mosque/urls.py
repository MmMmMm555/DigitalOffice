from django.urls import path

from apps.mosque.api_endpoints.Mosque.views import MosqueCreateView, MosqueListView, MosqueRetrieveView


urlpatterns = [
    # mosque
    path('create/', MosqueCreateView.as_view(), name='mosque_create'),
    path('list/', MosqueListView.as_view(), name='mosque_list'),
    path('single/<int:pk>', MosqueRetrieveView.as_view(), name='mosque_single'),
]