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
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'actual_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_website(self):
        regx = re.compile(
            '^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+(\.[a-z]{2,}){1,3}(#?\/?[a-zA-Z0-9#]+)*\/?(\?[a-zA-Z0-9-_]+=[a-zA-Z0-9-%]+&?)?$')
        if regx.match(self.cleaned_data.get('website')):
            return self.cleaned_data.get('website')

        raise ValidationError("Error encountered in website field.")


class UnitEditForm(forms.Form):
    pass
