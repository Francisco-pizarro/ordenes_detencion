# Ordenesdetencion/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
import re

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def clean_username(self):
        email = self.cleaned_data.get('username')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValidationError("El correo electrónico no tiene un formato válido.")
        return email
    
