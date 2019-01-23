from django import forms
from .models import Unit
from django.core.exceptions import ValidationError
import re


class UnitCreateForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = [
            'display_name',
            'actual_name',
        ]

        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. kg, ltr, mtr...'}),
            'actual_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. Kilogram, Liter, Meter...'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['display_name'].empty_label = 'e.g. kg, ltr, mtr...'
    #     self.fields['actual_name'].empty_label = 'e.g. Kilogram, Liter, Meter...'


class UnitEditForm(forms.Form):
    pass
