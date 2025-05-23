import pytest
from Ordenesdetencion.views import validaRut

@pytest.mark.parametrize("rut, esperado", [
    ("12.345.678-5", True),
    ("12345678-5", True),
    ("algasd123", False),
    ("00.000.000-0", False),
    ("11.111.111-1", False),
    ("17937114-6", True),
    ("abc-def-gh", False),
    ("1111111111", False)
])
def test_validaRut(rut, esperado):
    resultado = validaRut(rut)
    if resultado == esperado:
        print(f"Test paso -> RUT: {rut} | Esperado: {esperado} | Resultado: {resultado}")
    else:
        assert False
        
        
#pytest -s para visualizar los print expuesto en el codigo
#pytest solamente devulve resultado del test