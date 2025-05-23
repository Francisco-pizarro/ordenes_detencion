import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

Usuario = get_user_model()

@pytest.mark.django_db
def test_login_exitoso(client):
    Usuario.objects.create_user(email="usuario@correo.com", password="Clave1234")
    response = client.post(reverse('login'), {'email': 'usuario@correo.com', 'password': 'Clave1234'})
    print("STATUS CODE:", response.status_code)
    print("URL:", response.url if hasattr(response, "url") else "NO URL")
    print(response.content.decode())
    assert response.status_code == 302
    assert response.url == reverse('index')

@pytest.mark.django_db
def test_login_email_vacio(client):
    response = client.post(reverse('login'), {'email': '', 'password': 'Clave1234'}, follow=True)
    print(response.content.decode())
    assert "El campo correo electrónico es obligatorio." in response.content.decode()

@pytest.mark.django_db
def test_login_password_vacia(client):
    response = client.post(reverse('login'), {'email': 'usuario@correo.com', 'password': ''}, follow=True)
    print(response.content.decode())
    assert "El campo contraseña es obligatorio." in response.content.decode()

@pytest.mark.django_db
def test_login_email_invalido(client):
    response = client.post(reverse('login'), {'email': 'correo-invalido', 'password': 'Clave1234'}, follow=True)
    print(response.content.decode())
    assert "Debe ingresar un correo electrónico válido." in response.content.decode()

@pytest.mark.django_db
def test_login_credenciales_incorrectas(client):
    Usuario.objects.create_user(email="usuario@correo.com", password="Clave1234")
    response = client.post(reverse('login'), {'email': 'usuario@correo.com', 'password': 'claveIncorrecta'}, follow=True)
    print(response.content.decode())
    assert "Correo electrónico o contraseña incorrectos." in response.content.decode()

@pytest.mark.django_db
def test_login_usuario_inactivo(client):
    user = Usuario.objects.create_user(email="usuario@correo.com", password="Clave1234", is_active=False)
    response = client.post(reverse('login'), {'email': 'usuario@correo.com', 'password': 'Clave1234'}, follow=True)
    print(response.content.decode())
    assert "Su cuenta se encuentra inactiva. Contacte al administrador." in response.content.decode()

@pytest.mark.django_db
def test_login_email_no_registrado(client):
    response = client.post(reverse('login'), {'email': 'noexiste@correo.com', 'password': 'Clave1234'}, follow=True)
    print(response.content.decode())
    assert "Correo electrónico o contraseña incorrectos." in response.content.decode()
