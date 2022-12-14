from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
]
