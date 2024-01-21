# forms.py
from django import forms
from .models import Opinion, Destination
from crispy_forms.helper import FormHelper


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ["comment", "rating"]

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 1 or rating > 5:
            raise forms.ValidationError("La calificación debe estar entre 1 y 5")
        return rating


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ["name", "description", "photo"]
