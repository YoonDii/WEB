from .models import Info
from django import forms


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ["title", "summary", "running_time"]
