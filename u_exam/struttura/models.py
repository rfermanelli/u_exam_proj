from django.db import models

# Create your models here.
# Modello Dipartimento
class Dipartimento(models.Model):
    # segua una docstring di presentazione del modello:
    """Modello della entità Dipartimento dell'area Struttura organizzativa"""

    id_dipartimento = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    sede = models.CharField(max_length=100)

    # Meta è una classe interna che fornisce a Django i metadati sul modello:
    # 1) verbose_name_plural = definisce il nome plurale del modello nell'interfaccia admin,
    # senza questa opzione Django renderebbe il plurale in inglese scrivendo Dipartimentos
    # 2) ordering = definisce l'ordinamento di default nelle query,
    # con ['nome'] i risultati sono determinati in ordine alfabetico per nome.
    class Meta:
        verbose_name_plural = 'Dipartimenti'
        ordering = ['nome']
        managed = True          
        db_table = 'dipartimento'  

    def __str__(self):
        return self.nome

# Modello Corso di laurea
class CorsoDiLaurea(models.Model):
    # segua una docstring di presentazione del modello:
    """Modello della entità Corso di laurea dell'area Struttura organizzativa"""

    id_cdl = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, unique=True)
    classe_di_laurea = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=[('Triennale', 'Triennale'), ('Magistrale', 'Magistrale')])
    dipartimento = models.ForeignKey(Dipartimento, on_delete=models.CASCADE, related_name="corso_di_laurea")

    # Meta è una classe interna che fornisce a Django i metadati sul modello:
    # 1) verbose_name_plural = definisce il nome plurale del modello nell'interfaccia admin,
    # senza questa opzione Django renderebbe il plurale in inglese scrivendo CorsoDiLaureas
    # 2) ordering = definisce l'ordinamento di default nelle query,
    # con ['nome'] i risultati sono determinati in ordine alfabetico per nome.
    class Meta:
        verbose_name_plural = 'Corsi di laurea'
        ordering = ['nome']
        managed = True          
        db_table = 'corsodilaurea'

    def __str__(self):
        return self.nome
    

class Docente(models.Model):
    # segua una docstring di presentazione del modello:
    """Modello della entità Docente dell'area Struttura organizzativa"""

    id_docente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    cognome = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254, null=True, blank=True, default=None, verbose_name="Email del docente")
    ruolo = models.CharField(max_length=20)
    dipartimento = models.ForeignKey(Dipartimento, on_delete=models.CASCADE, related_name="docenti")

    # Meta è una classe interna che fornisce a Django i metadati sul modello:
    # 1) verbose_name_plural = definisce il nome plurale del modello nell'interfaccia admin,
    # senza questa opzione Django renderebbe il plurale in inglese scrivendo CorsoDiLaureas
    # 2) ordering = definisce l'ordinamento di default nelle query,
    # con ['nome'] i risultati sono determinati in ordine alfabetico per nome.
    class Meta:
        verbose_name_plural = 'Docenti'
        ordering = ['nome', 'cognome']
        managed = True          
        db_table = 'docente'

    def __str__(self):
        return self.nome + " " + self.cognome
    