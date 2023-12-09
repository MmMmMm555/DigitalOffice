from django.urls import path
from apps.friday_tesis.api_endpoints.tesis import views


urlpatterns = [
    path('create/', views.FridayTesisCreateView.as_view(), name='tesis_create'),
]
