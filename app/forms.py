# app/forms.py
from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__' # Или перечислите поля: ['companyname', 'contactname', ...]