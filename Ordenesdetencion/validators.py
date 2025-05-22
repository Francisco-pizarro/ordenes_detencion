import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MaxLengthPasswordValidator:
    def __init__(self, max_length=20):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _(f"La contraseña no puede tener más de {self.max_length} caracteres."),
                code='password_too_long',
            )

    def get_help_text(self):
        return _(f"Tu contraseña no puede tener más de {self.max_length} caracteres.")
    
class AlphanumericPasswordValidator:
    def validate(self, password, user=None):
        if not (re.search(r'[A-Za-z]', password) and re.search(r'\d', password)):
            raise ValidationError(
                _("La contraseña debe contener letras y números."),
                code='password_no_alphanumeric',
            )

    def get_help_text(self):
        return _("La contraseña debe contener letras y números.")