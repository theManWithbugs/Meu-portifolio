<<<<<<< HEAD
from django import forms 
from .models import *


class NomeSobrenomeForm(forms.ModelForm):
    class Meta:
        model = NomeUser
=======
from django import forms
from core import models 

class NomeSobrenomeForm(forms.ModelForm):
    class Meta:
        model = models.NomeUser
>>>>>>> 094a617d82c9131fa2dbec39e508b46cb2394086
        fields = '__all__'
        