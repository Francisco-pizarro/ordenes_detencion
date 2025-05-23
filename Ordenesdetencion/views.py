from itertools import cycle
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import Persona, Orden, MedidaCautelar
from django.contrib.auth import get_user_model

Usuario = get_user_model()

def validaRut(rut):
    rut = rut.upper()
    rut = rut.replace("-", "")
    rut = rut.replace(".", "")
    aux = rut[:-1]
    dv = rut[-1:]

    if not aux.isnumeric():
        return False
    if len(set(aux)) == 1:
        return False
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(revertido, factors))
    res = (-s) % 11

    if str(res) == dv:
        return True
    elif dv == "K" and res == 10:
        return True
    else:
        return False

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        print(f"POST data - email: '{email}', password: '{password}'")

        # Validar si está vacío
        if not email:
            print("ERROR: Falta email")
            messages.error(request, "El campo correo electrónico es obligatorio.")
            return render(request, 'registration/login.html')

        if not password:
            print("ERROR: Falta contraseña")
            messages.error(request, "El campo contraseña es obligatorio.")
            return render(request, 'registration/login.html')

        # Validar formato de email
        try:
            validate_email(email)
        except ValidationError:
            print("ERROR: Email inválido")
            messages.error(request, "Debe ingresar un correo electrónico válido.")
            return render(request, 'registration/login.html')

        user = authenticate(request, email=email, password=password)
        print(f"Usuario autenticado: {user}")

        if user is None:
            print("ERROR: Credenciales incorrectas")
            messages.error(request, "Correo electrónico o contraseña incorrectos.")
            return render(request, 'registration/login.html')

        if not user.is_active:
            print("ERROR: Usuario inactivo")
            messages.error(request, "Su cuenta se encuentra inactiva. Contacte al administrador.")
            return render(request, 'registration/login.html')

        # Login exitoso
        print("Login exitoso. Redirigiendo a index.")
        auth_login(request, user)
        return redirect('index')

    # GET o cualquier otro método HTTP
    print("GET request - mostrando formulario")
    return render(request, 'registration/login.html', {'just_posted': request.method == 'POST'})


@login_required
def index(request):
    if request.method == 'POST':
        rut = request.POST.get('txtRut')
        if validaRut(rut):
            rut = rut.replace(".", "")
            try:
                persona = Persona.objects.get(gls_rut=rut)
            except Persona.DoesNotExist:
                return render(request, 'verde.html')
            orden = Orden.objects.filter(persona_id=persona.id_persona)
            cautelar = MedidaCautelar.objects.filter(persona_id=persona.id_persona)
            if orden.exists():
                return render(request, 'rojo.html', {'persona': persona, 'orden': orden})
            elif cautelar.exists():
                return render(request, 'amarillo.html', {'persona': persona, 'cautelar': cautelar})
            else:
                return render(request, 'verde.html')
        else:
            return render(request, 'index.html', {'rutNoValido': 'El RUN ingresado no es válido.'})
    else:
        return render(request, 'index.html')
