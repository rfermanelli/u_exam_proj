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
    


# Definizione della classe di controllo del form con validazione più completa:
# class DipartimentoNew(forms.Form):
#     # 1. Validazione del tipo + parametri del campo
#     identificativo = forms.IntegerField(
#         min_value=101,          # deve essere maggiore di 100
#         max_value=9999,         # deve essere minore di 9999
#         required=True,          # campo obbligatorio
#         label="Identificativo",
#         error_messages={
#             'required': 'Il campo identificativo è obbligatorio.',
#             'min_value': 'Il valore deve essere maggiore di 100.',
#             'max_value': 'Il valore deve essere minore di 9999.',
#             'invalid': 'Inserisci un numero intero valido.',
#         }
#     )

#     nome = forms.CharField(
#         max_length=100,         # massimo 100 caratteri
#         min_length=3,           # minimo 3 caratteri
#         required=True,          # campo obbligatorio
#         label="Nome",
#         error_messages={
#             'required': 'Il campo nome è obbligatorio.',
#             'max_length': 'Il nome non può superare 100 caratteri.',
#             'min_length': 'Il nome deve avere almeno 3 caratteri.',
#         }
#     )

#     sede = forms.CharField(
#         max_length=100,
#         min_length=3,
#         required=True,
#         label="Sede",
#         error_messages={
#             'required': 'Il campo sede è obbligatorio.',
#             'max_length': 'La sede non può superare 100 caratteri.',
#             'min_length': 'La sede deve avere almeno 3 caratteri.',
#         }
#     )

#     # 2. Validazione custom sul singolo campo
#     def clean_identificativo(self):
#         identificativo = self.cleaned_data['identificativo']
#         # logica custom aggiuntiva rispetto ai parametri del campo
#         if identificativo % 2 == 0:
#             raise forms.ValidationError("L'identificativo deve essere un numero dispari.")
#         return identificativo

#     def clean_nome(self):
#         nome = self.cleaned_data['nome']
#         # controlla che il nome non contenga numeri
#         if any(char.isdigit() for char in nome):
#             raise forms.ValidationError("Il nome non può contenere numeri.")
#         # normalizza il dato: prima lettera maiuscola
#         return nome.capitalize()

#     def clean_sede(self):
#         sede = self.cleaned_data['sede']
#         # controlla che la sede non contenga numeri
#         if any(char.isdigit() for char in sede):
#             raise forms.ValidationError("La sede non può contenere numeri.")
#         return sede.capitalize()

#     # 3. Validazione che coinvolge più campi insieme
#     def clean(self):
#         cleaned_data = super().clean()
#         nome = cleaned_data.get('nome')
#         sede = cleaned_data.get('sede')
#         # controlla che nome e sede non siano uguali
#         if nome and sede and nome.lower() == sede.lower():
#             raise forms.ValidationError("Il nome e la sede non possono essere uguali.")
#         return cleaned_data
    

# Definizione della classe di controllo del form con validazione più completa e personalizzazione dei widget:
# class DipartimentoNew(forms.Form):
#     identificativo = forms.IntegerField(
#         # NumberInput è il widget di default per IntegerField
#         # lo specifichiamo esplicitamente per aggiungere attributi HTML
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',        # classe CSS di Bootstrap
#             'placeholder': 'Es. 101',       # testo di aiuto nel campo
#             'min': '101',                   # validazione HTML lato browser
#         }),
#         min_value=101,                      # validazione Django lato server
#         label="Identificativo",
#         error_messages={
#             'required': 'Il campo identificativo è obbligatorio.',
#             'min_value': 'Il valore deve essere maggiore di 100.',
#         }
#     )

#     nome = forms.CharField(
#         # di default CharField usa TextInput
#         # lo sostituiamo con Textarea per avere un campo più grande
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',        # classe CSS di Bootstrap
#             'placeholder': 'Nome del dipartimento',
#             'rows': 3,                      # altezza del textarea in righe
#             'cols': 40,                     # larghezza del textarea in colonne
#         }),
#         max_length=100,
#         min_length=3,
#         label="Nome",
#         error_messages={
#             'required': 'Il campo nome è obbligatorio.',
#         }
#     )

#     sede = forms.CharField(
#         # usiamo TextInput con attributi personalizzati
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Es. Roma, Milano...',
#             'maxlength': '100',             # validazione HTML lato browser
#         }),
#         max_length=100,
#         min_length=3,
#         label="Sede",
#         error_messages={
#             'required': 'Il campo sede è obbligatorio.',
#         }
#     )