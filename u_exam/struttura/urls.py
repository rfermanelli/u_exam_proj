from django.urls import path
from struttura.views import dipartimento_insert

urlpatterns = [
    path("dipartimento/new/", dipartimento_insert, name="pagina di insert del dipartimento")
]