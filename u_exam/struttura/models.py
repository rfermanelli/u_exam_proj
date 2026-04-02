from django.db import models

# Create your models here.
class Dipartimento(models.Model):
    id_dipartimento = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True)
    sede = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Dipartimenti'
        ordering = ['nome']

    def __str__(self):
        return self.nome
