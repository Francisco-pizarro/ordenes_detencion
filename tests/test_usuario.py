import re
import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

Usuario = get_user_model()

# Tests de contraseña: límites y particiones de equivalencia
@pytest.mark.parametrize("password,should_raise", [
    ("A234567", True),               # 7 caracteres, debe fallar (menor al mínimo)
    ("A2345678", False),             # 8 caracteres, válido (mínimo permitido)
    ("A23456789", False),            # 9 caracteres, válido
    ("ABCDEFGHIJ123456789", False),  # 19 caracteres, válido
    ("ABCDEFGHIJK123456789", False), # 20 caracteres, válido (máximo permitido)
    ("ABCDEFGHIJKL123456789", True), # 21 caracteres, debe fallar (mayor al máximo)
    ("123456789", True),             # Solo números, debe fallar (no cumple seguridad)
    ("abcdefghijk", True),           # Solo letras, debe fallar (no cumple seguridad)
    ("", True),                      # Vacía, debe fallar
])
@pytest.mark.django_db
def test_password_largos_y_formato(password, should_raise):
    if should_raise:
        with pytest.raises(ValidationError):
            validate_password(password)
    else:
        try:
            validate_password(password)
        except ValidationError:
            pytest.fail(f"Contraseña válida fue rechazada: {password}")

# Tests de emails: particiones de equivalencia
@pytest.mark.parametrize("email,should_raise", [
    ("usuario@correo.com", False),   # Válido
    ("correo-sin-arroba.com", True), # Sin @
    ("usuario@.com", True),          # Dominio inválido
    ("usuario@correo", True),        # Falta TLD
    ("@correo.com", True),           # Falta nombre usuario
    ("", True),                      # Vacío
])
def test_email_formato(email, should_raise):
    regex = r"[^@]+@[^@]+\.[^@]+"
    if should_raise:
        assert not re.match(regex, email)
    else:
        assert re.match(regex, email)

# Test de creación de usuario válido
@pytest.mark.django_db
def test_crear_usuario_valido():
    user = Usuario.objects.create_user(email="usuario@correo.com", password="Clave1234")
    assert user.email == "usuario@correo.com"
    assert user.check_password("Clave1234")
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser

# Test de email duplicado
@pytest.mark.django_db
def test_email_duplicado():
    Usuario.objects.create_user(email="usuario@correo.com", password="Clave1234")
    with pytest.raises(Exception):
        Usuario.objects.create_user(email="usuario@correo.com", password="OtraClave5678")

# Test de campo email obligatorio
@pytest.mark.django_db
def test_email_obligatorio():
    with pytest.raises(ValueError):
        Usuario.objects.create_user(email="", password="Clave1234")

# Test de campo password obligatorio
@pytest.mark.django_db
def test_password_obligatorio():
    with pytest.raises(ValueError, match="contraseña"):
        Usuario.objects.create_user(email="nuevo@correo.com", password=None)
