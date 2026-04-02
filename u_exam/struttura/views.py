from django.shortcuts import render

# import dell'oggetto HttpResponse
from django.http import HttpResponse

# Create your views here.
def dipartimento_insert(request):
    return HttpResponse("<h1>Questa è la funzione che opera una insert nella tabella dipartimento</h1>")
