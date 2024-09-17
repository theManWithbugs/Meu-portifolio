from django import forms
from core import models 

class NomeSobrenomeForm(forms.ModelForm):
    class Meta:
        model = models.NomeUser
        fields = '__all__'
        