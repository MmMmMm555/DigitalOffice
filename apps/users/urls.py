from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.api_endpoints.Login.views import LoginObtainTokenPairView
from apps.users.api_endpoints.Register.views import RegisterView

urlpatterns = [
    path('login/', LoginObtainTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view())
]
