from django.urls import path
from apps.friday_tesis.api_endpoints.tesis.views import FridayTesisCreateView
from apps.friday_tesis.api_endpoints.seen_api.views import FridayTesisImamReadView


urlpatterns = [
    path('create/', FridayTesisCreateView.as_view(), name='tesis_create'),
    path('seen/', FridayTesisImamReadView.as_view(), name='tesis_seen'),
]
