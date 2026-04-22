from django.contrib import admin

# Register your models here.
from .models import Ssd, Corso, Docenza, AnnoAccademico

admin.site.register(Ssd)
admin.site.register(Corso)
admin.site.register(Docenza)
admin.site.register(AnnoAccademico)
