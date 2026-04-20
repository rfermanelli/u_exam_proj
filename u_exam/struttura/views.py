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

# import del form DipartimentoNew
from .forms import DipartimentoNew
# Definizione della funzione controller del form DipartimentoNew:
def dipartimento_new(request):
    if request.method == 'POST':
        form = DipartimentoNew(request.POST)
        if form.is_valid():
            dipartimento = Dipartimento(
                id_dipartimento= form.cleaned_data['identificativo'], 
                nome=form.cleaned_data['nome'], 
                sede=form.cleaned_data['sede'])
            dipartimento.save()
            print(form.cleaned_data)
            print(f"testo: {form.cleaned_data['nome']}")
            return HttpResponse("<h1>Dipartimento aggiunto con successo</h1>")
    else:
        form = DipartimentoNew()

    context = {"form": form}
    return render(request, 'dipartimento_new.html', context)

