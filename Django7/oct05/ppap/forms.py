from .models import Ppap
from django import forms


class PpapForm(forms.ModelForm):
    class Meta:
        model = Ppap
        fields = ["title", "content"]
