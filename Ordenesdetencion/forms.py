from django import forms
from .models import BuscaRut

class BuscaRutForm(forms.ModelForm):
    class Meta:
        model = BuscaRut
        fields = ('rut',)