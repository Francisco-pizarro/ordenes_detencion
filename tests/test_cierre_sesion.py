import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.mark.django_db
def test_logout_protege_index(client):
    # Crear usuario
    email = 'test@test.com'
    password = '12345678'
    User.objects.create_user(email=email, password=password)

    # Simular login (sin pasar por tu vista)
    assert client.login(email=email, password=password)

    # Acceder a la vista protegida
    response = client.get('/')
    assert response.status_code == 200

    # Hacer logout manualmente
    client.logout()

    # Intentar acceder nuevamente
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.url  # redirige a login porque ya no hay sesión
