import re
import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

Usuario = get_user_model()

# Acá probamos la funcion de django create_user(), validamos si efectivamente crea un usuario segun los parametros que le mandamos
@pytest.mark.django_db
def test_crear_usuario_valido():
    user =  Usuario.objects.create_user(email="usuario@correo.com", password="Clave1234")
    assert user.email == "usuario@correo.com" # formato email y dominio correctos
    assert user.check_password("Clave1234") #Clave alfanumerica, de minimo 8 y maximo 20
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser

# Probar con un email de formato inválido, parametrize permite probar con diferentes valores, con esto podemos cubrir las CE de la variable email.
#CE1 fornmato no valido
#CE2 dominio invalido
#EC3 variable vacia
@pytest.mark.parametrize("email", [
    "correo-sin-arroba.com",
    "usuario@.com",
    ""
])
def test_email_formato_invalido(email):
    regex = r"[^@]+@[^@]+\.[^@]+"
    assert not re.match(regex, email)

#Cobertura de limites para el largo de caracteres que debe llevar la contraseña del usuario
# Limites negativos[7,21]
# Limites positivos[8,9,19,20]

@pytest.mark.django_db
def test_password_largo_7():
    with pytest.raises(ValidationError):
        validate_password("A234567")

@pytest.mark.django_db
def test_password_largo_8():
    try:
        validate_password("A2345678")
    except ValidationError:
        pytest.fail("Contraseña válida (8 caracteres) fue rechazada por un error inesperado")

@pytest.mark.django_db
def test_password_largo_9():
    try:
        validate_password("A23456789")
    except ValidationError:
        pytest.fail("Contraseña válida (9 caracteres) fue rechazada por un error inesperado" )

@pytest.mark.django_db
def test_password_largo_19():
    try:
        validate_password("ABCDEFGHIJ123456789")
    except ValidationError:
        pytest.fail("Contraseña válida (19 caracteres) fue rechazada por un error inesperado")

@pytest.mark.django_db
def test_password_largo_20():
    try:
        validate_password("ABCDEFGHIJK123456789")
    except ValidationError:
        pytest.fail("Contraseña válida (20 caracteres) fue rechazada por un error inesperado")

@pytest.mark.django_db
def test_password_largo_21():
    with pytest.raises(ValidationError):
        validate_password("ABCDEFGHIJKL123456789") 
        
@pytest.mark.django_db
def test_password_solo_numeros_rechazada():
    with pytest.raises(ValidationError):
        validate_password("123456789")

@pytest.mark.django_db
def test_password_solo_letras_rechazada():
    with pytest.raises(ValidationError):
        validate_password("abcdefghijk")
        
@pytest.mark.django_db
def test_email_duplicado():
    # Crear el primer usuario
    Usuario.objects.create_user(email="usuario@correo.com", password="Clave1234")
    # Intentar crear el segundo usuario con el mismo email
    with pytest.raises(Exception):
        Usuario.objects.create_user(email="usuario@correo.com", password="OtraClave5678")
