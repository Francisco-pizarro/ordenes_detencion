import pytest
from datetime import date, timedelta
from Ordenesdetencion.models import Persona, Pais, Comuna, Region, Actividad, EstadoCivil, Sexo
from django.core.exceptions import ValidationError

@pytest.fixture
def objetos_relacionados():
    pais = Pais.objects.create(gls_pais='Chile')
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

# Limites y equivalencias
limites = [
    (date(1919, 12, 31), True),                 # Debe fallar: antes del mínimo
    (date(1920, 1, 1), False),                  # Debe pasar: justo en el mínimo permitido
    (date(1920, 1, 2), False),                  # Debe pasar: apenas dentro del rango
    (date.today() - timedelta(days=1), False),  # Debe pasar: ayer
    (date.today(), False),                      # Debe pasar: hoy
    (date.today() + timedelta(days=1), True),   # Debe fallar: futuro
]

@pytest.mark.parametrize("nacimiento,should_raise", limites)
@pytest.mark.django_db
def test_fec_fecha_nacimiento_limites(nacimiento, should_raise, objetos_relacionados):
    persona = Persona(
        gls_rut='11111111-1',
        gls_apellido_paterno='Pérez',
        gls_apellido_materno='González',
        gls_nombres='Juan',
        fec_fecha_nacimiento=nacimiento,
        pais=objetos_relacionados['pais'],
        comuna=objetos_relacionados['comuna'],
        actividad=objetos_relacionados['actividad'],
        estado_civil=objetos_relacionados['estado_civil'],
        sexo=objetos_relacionados['sexo'],
    )
    if should_raise:
        with pytest.raises(ValidationError) as excinfo:
            persona.full_clean()
        assert "debe estar entre 1920" in str(excinfo.value)
    else:
        persona.full_clean()
