import pytest
from Ordenesdetencion.views import validaRut

@pytest.mark.parametrize("rut, esperado", [
    ("12.345.678-5", True),  # rut	RUT válido con puntos y guion	Válido	12.345.678-5
    ("12345678-5", True),  # rut	RUT válido sin puntos, con guion	Válido	12345678-5
    ("algasd123", False),  # rut	Cadena no numérica	Inválido	algasd123
    ("00.000.000-0", False), # rut	RUT con ceros repetidos	Inválido	00.000.000-0
    ("11.111.111-1", False), # rut	RUT con valores repetidos	Inválido	11.111.111-1
    ("17937114-6", True), # rut	RUT válido sin puntos ni guion	Válido	17937114-6
    ("abc-def-gh", False), # rut	Texto completamente inválido	Inválido	abc-def-gh
    ("1111111111", False) # rut	Número excesivo sin guion	Inválido	1111111111
])
def test_validaRut(rut, esperado):
    resultado = validaRut(rut)
    if resultado == esperado:
        print(f"Test paso -> RUT: {rut} | Esperado: {esperado} | Resultado: {resultado}")
    else:
        assert False
        
        
#pytest -s para visualizar los print expuesto en el codigo
#pytest solamente devulve resultado del test