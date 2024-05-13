from django.db import models

# Create your models here.
class Entitie(models.Model):
    class Meta:
        verbose_name = 'Categorie'

class Villain(models.Model):
    class Meta:
        verbose_name = 'Villain'