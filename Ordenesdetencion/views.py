from django.shortcuts import render
from .models import Persona, Orden, MedidaCautelar

# Create your views here.
def index(request):
    
    
    if request.method == 'POST':
        rut = request.POST.get('txtRut')
        if rut:      
            # 17123213-9 OD
            # 12223432-4 MC
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
            return render(request, 'index.html')            
    else:        
        return render(request, 'index.html')

