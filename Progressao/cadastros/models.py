from django.db import models

# Create your models here.
class Campo(models.Model):
    name = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    def __str__(self):
       return "{}({})".format(self.name,self.descricao)
class Atividade(models.Model):
       numero =models.BigIntegerField(verbose_name="número")
       descricao = models.CharField(max_length=150, verbose_name="Descrição")
       pontos = models.DecimalField(decimal_places=1,max_digits=4)
       detalhes = models.CharField(max_length=100)
       campo = models.ForeignKey(Campo, on_delete=models.PROTECT)
       def __str__(self):
           return "{}({})".format(self.numero,self.descricao)