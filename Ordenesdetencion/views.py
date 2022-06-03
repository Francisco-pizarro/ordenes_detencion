from django.shortcuts import render
from .models import Persona, Orden

# Create your views here.
def index(request):
    return render(request, 'index.html')

def resultado(request):
    rut='17123213-9'
    persona = Persona.objects.filter(gls_rut=rut)
    orden = Orden.objects.filter(id_orden=1)
    print([p.gls_nombres for p in persona])
    print([o.ruc for o in orden])
    return render(request, 'resultado.html', {'persona': persona,'orden': orden})

def resultadok(request):
    return render(request, 'resultadok.html')

def book_list(request):
    personas = Persona.objects.order_by('rut')
    return render('book_list.html', {'personas': personas})