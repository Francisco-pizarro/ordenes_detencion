from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .validators import MaxLengthPasswordValidator, AlphanumericPasswordValidator

Usuario = get_user_model()

def validar_login(email, password):
    if not email:
        return "El campo correo electrónico es obligatorio"
    if not password:
        return "El campo contraseña es obligatorio"

    try:
        validate_email(email)
    except ValidationError:
        return "Debe ingresar un correo electrónico válido"

    # Validar reglas personalizadas de contraseña
    try:
        MaxLengthPasswordValidator().validate(password)
        AlphanumericPasswordValidator().validate(password)
    except ValidationError as e:
        return e.messages[0]

    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return "Correo electrónico o contraseña incorrectos"

    if not usuario.check_password(password):
        return "Correo electrónico o contraseña incorrectos"

    if not usuario.is_active:
        return "Su cuenta se encuentra inactiva. Contacte al administrador."

    return "Login exitoso"
