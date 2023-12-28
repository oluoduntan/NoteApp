from django import forms
from .models import note

class noteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = ("title", "content")