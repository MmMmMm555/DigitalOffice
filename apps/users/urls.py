from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.users.api_endpoints.Login.views import LoginObtainTokenPairView
from apps.users.api_endpoints.Register.views import RegisterView
from apps.users.api_endpoints.List.views import UsersListView, UsersDetailView
from apps.users.api_endpoints.self_profile.views import UserSelfView

urlpatterns = [
    path('login/', LoginObtainTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view()),
    path('accounts/', UsersListView.as_view()),
    path('accounts/<int:pk>', UsersDetailView.as_view()),
    path('self_profile/', UserSelfView.as_view()),
]