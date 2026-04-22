from django.urls import path
from struttura.views import dipartimento_list, dipartimento_new
from struttura.views import corso_di_laurea_new

urlpatterns = [
    path("dipartimento/list/", dipartimento_list, name="dipartimento_list"),
    path("dipartimento/new/", dipartimento_new, name="dipartimento_new"),
    path("corso_di_laurea/new/", corso_di_laurea_new, name="corso_di_laurea_new")
]
