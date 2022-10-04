from django import forms
from .models import Ppap


class PpapForm(forms.ModelForm):
    class Meta:
        model = Ppap
        fields = ["title", "content"]
