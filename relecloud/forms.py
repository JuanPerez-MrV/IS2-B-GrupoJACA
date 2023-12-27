# forms.py
from django import forms
from .models import Opinion, Destination
from crispy_forms.helper import FormHelper


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ["comment", "rating"]


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ["name", "description", "photo"]
