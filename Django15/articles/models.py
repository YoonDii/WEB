from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from pjt.settings import AUTH_USER_MODEL

# Create your models here.
"""
게시판 기능 
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/시간)
"""
# 1. 모델 설계 (DB 스키마 설계)
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Admin(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(
        default="images/default_image.jpeg",
        upload_to="images/",
        blank=True,
    )
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=14)
    camp_type = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    active_day = models.CharField(max_length=10)
    homepage = models.CharField(max_length=40, blank=True)
    reservation = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    geography = models.CharField(max_length=20)


class Photo(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    auser = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(
        default="photos/default_image.jpeg",
        upload_to="photos/",
        blank=True,
    )
