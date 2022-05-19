from django.urls import path
from .views import check_user, register, login_view, logout_view, register_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

app_name = "users"

urlpatterns = [
    path('check-user', check_user),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('register', register, name="register"),
    path('pass-res', PasswordResetView.as_view(), name="pass_res"),
    path('custom-login', login_view, name="custom_login"),
    path('custom-logout', logout_view, name="custom_logout"),
    path('custom-register', register_view, name="custom_register")
]
