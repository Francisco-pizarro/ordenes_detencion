# tests/test_login.py

import pytest
from django.contrib.auth import get_user_model
from Ordenesdetencion.services import validar_login

Usuario = get_user_model()

@pytest.mark.django_db
def test_login_exitoso():
    Usuario.objects.create_user(email="test@test.cl", password="Clave123")
    assert validar_login("test@test.cl", "Clave123") == "Login exitoso"

@pytest.mark.django_db
def test_login_usuario_inactivo():
    Usuario.objects.create_user(email="test@test.cl", password="Clave123", is_active=False)
    assert validar_login("test@test.cl", "Clave123") == "Su cuenta se encuentra inactiva. Contacte al administrador."

def test_login_email_vacio():
    assert validar_login("", "Clave123") == "El campo correo electrónico es obligatorio"

def test_login_password_vacia():
    assert validar_login("test@test.cl", "") == "El campo contraseña es obligatorio"

def test_login_email_mal_formado():
    assert validar_login("bad@@email", "Clave123") == "Debe ingresar un correo electrónico válido"

def test_login_password_invalida_larga():
    password = "Clave12345678901234567890"
    assert validar_login("test@test.cl", password) == "La contraseña no puede tener más de 20 caracteres."

def test_login_password_sin_numeros():
    assert validar_login("test@test.cl", "mmmmmmmmm") == "La contraseña debe contener letras y números."

@pytest.mark.django_db
def test_login_usuario_no_existe():
    assert validar_login("noexiste@test.cl", "Clave123") == "Correo electrónico o contraseña incorrectos"

@pytest.mark.django_db
def test_login_password_incorrecta():
    Usuario.objects.create_user(email="test@test.cl", password="Clave123")
    assert validar_login("test@test.cl", "Clave12344") == "Correo electrónico o contraseña incorrectos"
