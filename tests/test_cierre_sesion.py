import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.mark.django_db
# TEST Equivalencia usuario autenticado
def test_logout_protege_index(client):
    # Crear usuario              var         clase equivalencia     estado     represenntante 
    email = 'test@test.com'  #Autenticación	 Usuario autenticado	Válido	Login con email y password
    password = '12345678'
    User.objects.create_user(email=email, password=password)

    # Simular login (sin pasar por view login)                   
    assert client.login(email=email, password=password)  

    # Acceder a la vista protegida        
    response = client.get('/')        
    assert response.status_code == 200

    # Hacer logout manualmente      
    client.logout() #           

    # Intentar acceder nuevamente
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.url 

