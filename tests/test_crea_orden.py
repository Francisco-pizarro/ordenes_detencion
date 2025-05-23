import pytest
from datetime import date
from Ordenesdetencion.models import Orden, Delito, Tribunal, Persona, Pais, Comuna, Region, Actividad, EstadoCivil, Sexo
from django.core.exceptions import ValidationError

@pytest.fixture
def persona_relacionada():
    pais = Pais.objects.create(gls_pais='Chile')
    region = Region.objects.create(gls_region='Metropolitana', pais=pais)
    comuna = Comuna.objects.create(gls_comuna='Santiago', region=region)
    actividad = Actividad.objects.create(gls_actividad='Test')
    estado_civil = EstadoCivil.objects.create(gls_estado_civil='Soltero')
    sexo = Sexo.objects.create(gls_sexo='Masculino')
    persona = Persona.objects.create(
        gls_rut='11111111-1',
        gls_apellido_paterno='Pérez',
        gls_apellido_materno='González',
        gls_nombres='Juan',
        fec_fecha_nacimiento=date(1985, 5, 15),
        pais=pais,
        comuna=comuna,
        actividad=actividad,
        estado_civil=estado_civil,
        sexo=sexo,
    )
    return persona

@pytest.fixture
def objetos_relacionados(persona_relacionada):
    delito = Delito.objects.create(gls_delito='Robo')
    tribunal = Tribunal.objects.create(gls_tribunal='Tribunal Supremo', comuna=persona_relacionada.comuna)
    return {
        'delito': delito,
        'tribunal': tribunal,
    }

# Limites y equivalencias
valores = [
    ('99999999', True),        # Justo debajo del límite inferior
    ('100000000', False),      # Justo en el límite inferior
    ('100000001', False),      # Apenas dentro del rango
    ('999999999', False),      # Justo en el límite superior permitido
    ('1000000000', False),     # Justo en el límite superior
    ('1000000001', True),      # Por sobre el límite superior (no permitido)
]

@pytest.mark.parametrize("ruc,should_raise", valores)
@pytest.mark.django_db
def test_ruc_orden_limites(ruc, should_raise, persona_relacionada, objetos_relacionados):
    orden = Orden(
        ruc=ruc,
        fecha_orden=date(2023, 5, 1),
        resolucion='Resolución válida',
        delito=objetos_relacionados['delito'],
        persona=persona_relacionada,
        tribunal=objetos_relacionados['tribunal'],
    )
    if should_raise:
        with pytest.raises(ValidationError) as excinfo:
            orden.full_clean()
        assert "debe estar entre 100,000,000 y 1,000,000,000" in str(excinfo.value)
    else:
        orden.full_clean()
