from django import forms
from .models import Item


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'iname',
            'unit',
            'price',
        ]
        widgets = {
            'iname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
            'unit': forms.Select(attrs={'class': 'form-control', }),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit'].empty_label = 'Select Unit'
