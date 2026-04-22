from django.db import models
from struttura.models import Docente 

# Create your models here.
class Ssd(models.Model):
    # segua una docstring di presentazione del modello:
    """Modello della entità SSD dell'area Offerta formativa"""

    codice_ssd = models.CharField(primary_key=True, max_length=10)
    descrizione = models.CharField(max_length=255)
    
    # Meta è una classe interna che fornisce a Django i metadati sul modello:
    # 1) verbose_name_plural = definisce il nome plurale del modello nell'interfaccia admin,
    # senza questa opzione Django renderebbe il plurale in inglese scrivendo CorsoDiLaureas
    # 2) ordering = definisce l'ordinamento di default nelle query,
    # con ['nome'] i risultati sono determinati in ordine alfabetico per nome.
    class Meta:
        verbose_name_plural = 'SSD'
        ordering = ['codice_ssd']
        managed = True          
        db_table = 'ssd'

    def __str__(self):
        return self.codice_ssd
    

class Corso(models.Model):
    # segua una docstring di presentazione del modello:
    """Modello della entità Corso dell'area Offerta formativa"""

    id_corso = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    ssd = models.ForeignKey(Ssd, on_delete=models.CASCADE, related_name="corsi")
    cfu = models.CharField(max_length=10)
    anno_di_corso = models.CharField(max_length=10)
    semestre =  models.CharField(max_length=10)
    
    # Meta è una classe interna che fornisce a Django i metadati sul modello:
    # 1) verbose_name_plural = definisce il nome plurale del modello nell'interfaccia admin,
    # senza questa opzione Django renderebbe il plurale in inglese scrivendo CorsoDiLaureas
    # 2) ordering = definisce l'ordinamento di default nelle query,
    # con ['nome'] i risultati sono determinati in ordine alfabetico per nome.
    class Meta:
        verbose_name_plural = 'Corsi'
        ordering = ['nome']
        managed = True          
        db_table = 'corso'

    def __str__(self):
        return self.nome
    
class AnnoAccademico(models.Model):
    # segua una docstring di presentazione del modello:
    """Modello della entità Anno accademico dell'area Offerta formativa"""

    id_anno_accademico = models.IntegerField(primary_key=True)
    anno_inizio = models.IntegerField()
    anno_fine = models.IntegerField()
    stato = models.CharField(max_length=1, choices=[('A', 'Attivo'), ('C', 'Concluso'), ('F', 'Futuro'), ('I', 'In preparazione')], default='A')
    
    # Meta è una classe interna che fornisce a Django i metadati sul modello:
    # 1) verbose_name_plural = definisce il nome plurale del modello nell'interfaccia admin,
    # senza questa opzione Django renderebbe il plurale in inglese scrivendo CorsoDiLaureas
    # 2) ordering = definisce l'ordinamento di default nelle query,
    # con ['nome'] i risultati sono determinati in ordine alfabetico per nome.
    class Meta:
        verbose_name_plural = 'Anni accademici'
        ordering = ['stato', 'anno_inizio']
        managed = True          
        db_table = 'anno_accademico'

    def __str__(self):
        return self.stato + " " + str(self.anno_inizio) + "/" + str(self.anno_fine)
    

class Docenza(models.Model):
    # segua una docstring di presentazione del modello:
    """Modello della entità Docenza dell'area Offerta formativa"""

    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="docenze")
    corso = models.ForeignKey(Corso, on_delete=models.CASCADE, related_name="docenze")
    anno_accademico = models.ForeignKey(AnnoAccademico, on_delete=models.CASCADE, related_name="docenze")
    titolare = models.BooleanField(default=False)
    
    # Meta è una classe interna che fornisce a Django i metadati sul modello:
    # 1) verbose_name_plural = definisce il nome plurale del modello nell'interfaccia admin,
    # senza questa opzione Django renderebbe il plurale in inglese scrivendo CorsoDiLaureas
    # 2) ordering = definisce l'ordinamento di default nelle query,
    # con ['nome'] i risultati sono determinati in ordine alfabetico per nome.
    class Meta:
        verbose_name_plural = 'Docenze'
        ordering = ['id_docente', 'id_corso', 'id_anno_accademico', 'titolare']
        managed = True          
        db_table = 'docenza'

    def __str__(self):
        return self.id_docente.__str__() + " - " + self.id_corso.__str__() + " - " + self.id_anno_accademico.__str__() + " - " + ("Titolare" if self.titolare else "Non titolare")
    
