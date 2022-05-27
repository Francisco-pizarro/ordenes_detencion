from django.shortcuts import render
from Ordenesdetencion.models import Persona

# Create your views here.
def index(request):
    return render(request, 'index.html')

def resultado(request):
    return render(request, 'resultado.html')

def resultadok(request):
    return render(request, 'resultadok.html')

def book_list(request):
    personas = Persona.objects.order_by('rut')
    return render('book_list.html', {'personas': personas})