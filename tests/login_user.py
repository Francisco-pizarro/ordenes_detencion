import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

Usuario = get_user_model()

#debemos crear un usuario para simular si entrada al sistema.
@pytest.mark.django_db
def test_login_usuario_valido_activo(client):
    Usuario.objects.create_user(email="test@test.cl", password="Clave123")
    response = client.post(reverse('login'), {
        'email': 'test@test.cl',
        'password': 'Clave123'
    })
    assert response.status_code == 302
    assert response.url == reverse('index')

@pytest.mark.django_db
def test_login_usuario_valido_inactivo(client):
    Usuario.objects.create_user(email="test@test.cl", password="Clave123", is_active=False)
    response = client.post(reverse('login'), {
        'email': 'test@test.cl',
        'password': 'Clave123'
    })
    assert "cuenta se encuentra inactiva" in response.content.decode().lower()

@pytest.mark.django_db
def test_login_email_no_registrado(client):
    response = client.post(reverse('login'), {
        'email': 'test@test.cl',
        'password': 'Clave123'
    })
    assert "correo electrónico o contraseña incorrectos" in response.content.decode().lower()

@pytest.mark.django_db
def test_login_contraseña_incorrecta(client):
    Usuario.objects.create_user(email="test@test.cl", password="Correcta123")
    response = client.post(reverse('login'), {
        'email': 'test@test.cl',
        'password': 'Incorrecta'
    })
    assert "correo electrónico o contraseña incorrectos" in response.content.decode().lower()

@pytest.mark.django_db
def test_login_email_formato_invalido(client):
    response = client.post(reverse('login'), {
        'email': 'test@@test.cl',
        'password': 'Clave123'
    })
    assert "debe ingresar un correo electrónico válido" in response.content.decode().lower()

@pytest.mark.django_db
def test_login_campos_vacios(client):
    response = client.post(reverse('login'), {
        'email': '',
        'password': ''
    })
    content = response.content.decode().lower()
    assert "el campo correo electrónico es obligatorio" in content or "el campo contraseña es obligatorio" in content
