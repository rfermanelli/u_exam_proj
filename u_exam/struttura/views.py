from django.shortcuts import render

# import dell'oggetto HttpResponse
from django.http import HttpResponse
# import dell'oggetto render per renderizzare i template
from django.shortcuts import render

# import degli oggetti model
from .models import Dipartimento, CorsoDiLaurea

# Create your views here.
def dipartimento_list(request):
    # dipartimenti = []
    # for dip in Dipartimento.objects.all():
    #     dipartimenti.append(dip.nome)
    # print(dipartimenti)
    # return HttpResponse("Dipartimenti: " + ", ".join(dipartimenti))
    dipartimenti = Dipartimento.objects.all()
    corsi_di_laurea = CorsoDiLaurea.objects.all()
    
    context = {
        'dipartimenti': dipartimenti,
        'corsi_di_laurea': corsi_di_laurea
    }
    # return render(request, 'struttura/dipartimento_list.html', {'dipartimenti': dipartimenti})
    return render(request, 'dipartimento/dipartimento_list.html', context)
