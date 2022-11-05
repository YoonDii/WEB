from django import forms
from .models import Article, Comment, Admin, Photo


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = (
            "name",
            "image",
            "address",
            "contact",
            "camp_type",
            "season",
            "active_day",
            "reservation",
            "geography",
        )


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("image",)
