from django import forms
from .models import Transactions


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'cname',
            'itemname',
            'quantity',
            'total',
        ]

        widgets = {
            'cname': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'itemname': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Item'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cname'].empty_label = "Customer Name"
        self.fields['itemname'].empty_label = "Item Name"
        # self.fields['cname'].widget.attrs['class'] = "form-control"
