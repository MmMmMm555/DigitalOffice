from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import MyObtainTokenPairView, RegisterView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view())
]
