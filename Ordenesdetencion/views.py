from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def resultado(request):
    return render(request, 'resultado.html')