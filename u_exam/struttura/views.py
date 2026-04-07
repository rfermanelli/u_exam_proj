from django.shortcuts import render

# import dell'oggetto HttpResponse
from django.http import HttpResponse

# import degli oggetti model
from .models import Dipartimento

# Create your views here.
def dipartimento_list(request):
    dipartimenti = []
    for dip in Dipartimento.objects.all():
        dipartimenti.append(dip.nome)
    print(dipartimenti)
    return HttpResponse("Dipartimenti: " + ", ".join(dipartimenti))