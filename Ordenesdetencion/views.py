from django.shortcuts import render
from Ordenesdetencion.models import Persona

# Create your views here.
def index(request):
    return render(request, 'index.html')

def resultado(request):
    
    persona = Persona.objects.all()
    data = {
        'persona': persona
    }
    return render(request, 'resultado.html', data)

def resultadok(request):
    return render(request, 'resultadok.html')

def book_list(request):
    personas = Persona.objects.order_by('rut')
    return render('book_list.html', {'personas': personas})