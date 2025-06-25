import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_logout_y_redirecciona_a_login(client):
    # Crear usuario y autenticar
    usuario = User.objects.create_user(email='test@test.com', password='12345678')
    client.force_login(usuario)  # más directo que client.login

    # Accede a una vista protegida (antes del logout)
    response = client.get('/')
    assert response.status_code == 200

    # Hacer logout
    client.logout()

    # Accede nuevamente a la misma vista
    response = client.get('/')
    assert response.status_code == 302  # redirige
    assert '/login' in response.url     # verifica redirección a login
