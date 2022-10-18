from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("<int:pk>/", views.detail, name="detail"),
    path("delete/", views.delete, name="delete"),
    path("chagne_password/", views.change_password, name="change_password"),
]
