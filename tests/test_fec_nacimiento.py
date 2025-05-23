import pytest
from datetime import date, timedelta
from Ordenesdetencion.models import Persona, Pais, Comuna, Region, Actividad, EstadoCivil, Sexo
from django.core.exceptions import ValidationError

@pytest.fixture
def objetos_relacionados():
    pais = Pais.objects.create(gls_pais='1')
    region = Region.objects.create(gls_region='Metropolitana', pais=pais)
    comuna = Comuna.objects.create(gls_comuna='Santiago', region=region)
    actividad = Actividad.objects.create(gls_actividad='Test')
    estado_civil = EstadoCivil.objects.create(gls_estado_civil='Soltero')
    sexo = Sexo.objects.create(gls_sexo='Masculino')
    return {
        'pais': pais,
        'comuna': comuna,
        'actividad': actividad,
        'estado_civil': estado_civil,
        'sexo': sexo,
    }

@pytest.mark.django_db
def test_fecha_nacimiento_valida(objetos_relacionados):
    persona = Persona(
        gls_rut='11111111-1',
        gls_apellido_paterno='Pérez',
        gls_apellido_materno='González',
        gls_nombres='Juan',
        fec_fecha_nacimiento=date(1985, 5, 15),
        pais=objetos_relacionados['pais'],
        comuna=objetos_relacionados['comuna'],
        actividad=objetos_relacionados['actividad'],
        estado_civil=objetos_relacionados['estado_civil'],
        sexo=objetos_relacionados['sexo'],
    )
    persona.full_clean()  # No debe lanzar error

@pytest.mark.django_db
def test_fecha_nacimiento_antigua(objetos_relacionados):
    persona = Persona(
        gls_rut='22222222-2',
        gls_apellido_paterno='Gómez',
        gls_apellido_materno='López',
        gls_nombres='Ana',
        fec_fecha_nacimiento=date(1910, 1, 1),
        pais=objetos_relacionados['pais'],
        comuna=objetos_relacionados['comuna'],
        actividad=objetos_relacionados['actividad'],
        estado_civil=objetos_relacionados['estado_civil'],
        sexo=objetos_relacionados['sexo'],
    )
    with pytest.raises(ValidationError) as excinfo:
        persona.full_clean()
    assert "debe estar entre 1920" in str(excinfo.value)

@pytest.mark.django_db
def test_fecha_nacimiento_futura(objetos_relacionados):
    future_date = date.today() + timedelta(days=1)
    persona = Persona(
        gls_rut='33333333-3',
        gls_apellido_paterno='Martínez',
        gls_apellido_materno='Ruiz',
        gls_nombres='Pedro',
        fec_fecha_nacimiento=future_date,
        pais=objetos_relacionados['pais'],
        comuna=objetos_relacionados['comuna'],
        actividad=objetos_relacionados['actividad'],
        estado_civil=objetos_relacionados['estado_civil'],
        sexo=objetos_relacionados['sexo'],
    )
    with pytest.raises(ValidationError) as excinfo:
        persona.full_clean()
    assert "debe estar entre 1920" in str(excinfo.value)
