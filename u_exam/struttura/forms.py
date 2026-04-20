# Importazione del modulo forms:
from django import forms

# Definizione della classe di controllo del form:
class DipartimentoNew(forms.Form):
    identificativo = forms.IntegerField()
    nome = forms.CharField(max_length=100)
    sede = forms.CharField(max_length=100)
    
