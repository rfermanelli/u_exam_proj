from django.urls import path
from struttura.views import dipartimento_list, dipartimento_new
from struttura.views import corso_di_laurea_new

urlpatterns = [
    path("dipartimento/list/", dipartimento_list, name="pagina di visualizzazione dei dipartimenti"),
    path("dipartimento/new/", dipartimento_new, name="pagina di aggiunta di un nuovo dipartimento"),
    path("corso_di_laurea/new/", corso_di_laurea_new, name="pagina di aggiunta di un nuovo corso di laurea")
]
