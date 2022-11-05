from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

# from .models import User
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")
        exclude = (
            "phone",
            "kakao_id",
            "kakao_nickname",
        )
        labels = {
            "phone": "휴대폰",
        }
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "'-' 를 제외하고 입력해주세요.",
                    "style": "width: 100%; resize: none;",
                }
            ),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")
