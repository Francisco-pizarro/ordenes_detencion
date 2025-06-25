from Ordenesdetencion.views import validaRut

def test_valida_rut_valido():
    rut = "12.345.678-5" 
    resultado = validaRut(rut)
    assert resultado is True, f"Se esperaba que el RUT '{rut}' fuera válido, pero fue rechazado."

def test_valida_rut_invalido():
    rut = "12.345.678-9" 
    resultado = validaRut(rut)
    assert resultado is False, f"Se esperaba que el RUT '{rut}' fuera inválido, pero fue aceptado."
