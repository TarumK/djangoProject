from django import forms
from .models import Town, Street


class AddressForm(forms.Form):


    name = forms.ModelChoiceField(queryset=Town.objects.all(), label='Город')
    # street = forms.ModelChoiceField(choices=ulica, label='Улица')
