# URL설정을 app 단위로!

from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path("<int:pk>/like/", views.like, name="like"),
    path("admin_create/", views.admin_create, name="admin_create"),
    path("<int:hot_pk>/hotplace", views.hotplace, name="hotplace"),
]
