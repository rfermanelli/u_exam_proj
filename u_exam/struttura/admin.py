from django.contrib import admin

# Register your models here.
from .models import CorsoDiLaurea, Dipartimento

admin.site.register(CorsoDiLaurea)
admin.site.register(Dipartimento)       
