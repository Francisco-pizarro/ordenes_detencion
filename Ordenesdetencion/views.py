
from itertools import cycle
from django.shortcuts import render
from .models import Persona, Orden, MedidaCautelar
from django.contrib.auth.decorators import login_required



@login_required()
def index(request):
    if request.method == 'POST':
        rut = request.POST.get('txtRut')
        if validaRut(rut):
            rut = rut.replace(".","")    
            
            try:                
                persona = Persona.objects.get(gls_rut=rut)
            except Persona.DoesNotExist:
                return render(request, 'verde.html')           

            orden = Orden.objects.filter(persona_id_persona=persona.id_persona)
            cautelar = MedidaCautelar.objects.filter(persona_id_persona=persona.id_persona)
            if orden:
                return render(request, 'rojo.html', {'persona': persona,'orden': orden})
            else:                
                if cautelar:
                    return render(request, 'amarillo.html', {'persona': persona,'cautelar': cautelar})
                else:
                    return render(request, 'verde.html')            
        else:
            return render(request, 'index.html',{'rutNoValido':'El RUN ingresado no es válido.'})            
    else:        
        return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')



def validaRut(rut):
    rut = rut.upper()
    rut = rut.replace("-","")
    rut = rut.replace(".","")
    aux = rut[:-1]
    dv = rut[-1:]
 
    if not aux.isnumeric():
        return False
    revertido = map(int, reversed(str(aux)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(revertido,factors))
    res = (-s)%11

    if str(res) == dv:
        return True
    elif dv=="K" and res==10:
        return True
    else:
        return False



