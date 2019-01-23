from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'cname',
            'address',
            'phone_no',
        ]
        widgets = {
            'cname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }
