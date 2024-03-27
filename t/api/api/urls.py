from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts import views

urlpatterns = [
    # ... other URLs
    path("api/register/", views.UserCreateView.as_view(), name="register"),
    path("api/login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/logout/", views.LogoutView.as_view(), name="logout"),
]
