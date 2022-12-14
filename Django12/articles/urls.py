from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
    path("comments/<int:pk>", views.comment_create, name="comment_create"),
    path(
        "<int:article_pk>/comments/<int:comment_pk>/delete",
        views.comments_delete,
        name="comments_delete",
    ),
    path(
        "<int:article_pk>/comments/<int:comment_pk>/update",
        views.comments_update,
        name="comments_update",
    ),
]
