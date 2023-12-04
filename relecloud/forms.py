from django import forms
from crispy_forms.helper import FormHelper
from .models import Opinion


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ["name", "comment", "rating"]
