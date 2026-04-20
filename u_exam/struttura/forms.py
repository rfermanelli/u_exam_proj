# Importazione del modulo forms:
from django import forms

# Definizione della classe di controllo del form:
class DipartimentoNew(forms.Form):
    identificativo = forms.IntegerField()
    nome = forms.CharField(max_length=100)
    sede = forms.CharField(max_length=100)

    def clean_identificativo(self):
        identificativo = self.cleaned_data['identificativo']
        if identificativo <= 100:
            raise forms.ValidationError("L'identificatore deve essere maggiore di 100.")
        return identificativo
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 3:
            raise forms.ValidationError("Il nome deve essere lungo almeno 3 caratteri.")
        return nome
    
    def clean_sede(self):
        sede = self.cleaned_data['sede']
        if len(sede) < 3:
            raise forms.ValidationError("La sede deve essere lunga almeno 3 caratteri.")
        return sede
    