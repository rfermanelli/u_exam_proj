from django.urls import path
from struttura.views import dipartimento_list

urlpatterns = [
    path("dipartimento/list/", dipartimento_list, name="pagina di visualizzazione dei dipartimenti"),
]
