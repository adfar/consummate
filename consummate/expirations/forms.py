from django import forms
from .models import Expiration, Food

class ExpirationForm(forms.Form):
    upc = forms.CharField(max_length=4)
    expiration_date = forms.DateField()