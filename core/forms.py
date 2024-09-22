from django import forms 
from .models import *


class NomeSobrenomeForm(forms.ModelForm):
    class Meta:
        model = NomeUser
        fields = '__all__'
        