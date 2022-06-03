from django.shortcuts import render
from .models import Persona, Orden

# Create your views here.
def index(request):
    
    
    if request.method == 'POST':
        rut = request.POST.get('txtRut')
        if rut:        
            print('rut1:-'+rut+'-')        
            #rut='17123213-9'
            persona = Persona.objects.filter(gls_rut=rut)[0]
            print('id_persona: '+str(persona.id_persona))
            orden = Orden.objects.filter(persona_id_persona=persona.id_persona)
            return render(request, 'resultado.html', {'persona': persona,'orden': orden})
        else:
            return render(request, 'index.html')            
    else:        
        return render(request, 'index.html')



def book_list(request):
    personas = Persona.objects.order_by('rut')
    return render('book_list.html', {'personas': personas})