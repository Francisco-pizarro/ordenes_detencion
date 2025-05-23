import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from Ordenesdetencion.models import Persona, Orden, MedidaCautelar, Pais, Comuna, Actividad, EstadoCivil, Sexo, Delito, Tribunal, Region
from datetime import date

User = get_user_model()

@pytest.mark.django_db
@pytest.mark.parametrize("con_orden, con_cautelar, template_esperado", [
    (True, False, 'rojo.html'),
    (False, True, 'amarillo.html'),
    (False, False, 'verde.html'),
])
def test_busqueda_por_rut(client, con_orden, con_cautelar, template_esperado):
    # Crear usuario usando email
    User.objects.create_user(
        email='test@test.com',
        password='12345678'
    )

    # Intentar login con email y password
    logged_in = client.login(email='test@test.com', password='12345678')
    assert logged_in, "Error Login"

    rut = '17.937.114-6'  # RUT con guion y sin puntos
    rut_limpio = rut.replace(".", "")

    # Crear datos relacionados mínimos necesarios para FK
    pais = Pais.objects.create(gls_pais="Chile")
    region = Region.objects.create(gls_region="Metropolitana", pais=pais)
    comuna = Comuna.objects.create(gls_comuna="Santiago", region=region)
    actividad = Actividad.objects.create(gls_actividad="Actividad X")
    estado_civil = EstadoCivil.objects.create(gls_estado_civil="Soltero")
    sexo = Sexo.objects.create(gls_sexo="Masculino")


    persona = Persona.objects.create(
        gls_rut=rut_limpio,
        gls_apellido_paterno="Perez",
        gls_apellido_materno="Gonzalez",
        gls_nombres="Juan",
        fec_fecha_nacimiento=date(1990, 1, 1),
        gls_depto="Depto 1",
        gls_calle="Calle Falsa",
        gls_numero_direccion="123",
        pais=pais,
        comuna=comuna,
        actividad=actividad,
        estado_civil=estado_civil,
        sexo=sexo,
    )

    delito = Delito.objects.create(gls_delito="Robo")
    tribunal = Tribunal.objects.create(gls_tribunal="Tribunal Santiago", comuna=comuna)

    if con_orden:
        Orden.objects.create(
            ruc="RUC1234",
            fecha_orden=date.today(),
            resolucion="Resolucion ejemplo",
            delito=delito,
            persona=persona,
            tribunal=tribunal
        )
    if con_cautelar:
        MedidaCautelar.objects.create(
            ruc="RUC5678",
            gls_medida_cautelar="Medida ejemplo",
            resolucion="Resolucion ejemplo",
            fecha=date.today(),
            persona=persona,
            tribunal=tribunal
        )

    response = client.post(reverse('index'), {'txtRut': rut})

    assert response.status_code == 200
    assert template_esperado in [t.name for t in response.templates]
