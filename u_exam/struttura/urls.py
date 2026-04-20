from django.urls import path
from struttura.views import dipartimento_list, dipartimento_new

urlpatterns = [
    path("dipartimento/list/", dipartimento_list, name="pagina di visualizzazione dei dipartimenti"),
    path("dipartimento/new/", dipartimento_new, name="pagina di aggiunta di un nuovo dipartimento")
]
