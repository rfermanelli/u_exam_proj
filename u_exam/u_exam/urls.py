"""
URL configuration for u_exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# import della funzione dipartimento_insert definita nel modulo view.py della app struttura
#from struttura.views import dipartimento_insert

# import del modulo views.py della app struttura
from struttura import views as struttura_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # corrispondenza tra la funzione dipartimento_insert definita nel modulo view.py della app struttura 
    # e l'URL relativo
    #path("dipartimento/new/", dipartimento_insert, name="pagina di insert del dipartimento"),
    #path("dipartimento/new/", struttura_views.dipartimento_insert, name="pagina di insert del dipartimento"),

    # path globale del modulo views.py della app struttura
    path("struttura/", include('struttura.urls'))

]
