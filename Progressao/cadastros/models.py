from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os

def user_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.progresso.id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    return os.path.join('uploads', 'comprovantes', str(instance.progresso.id), filename)
# Create your models here.
class Campo(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
def __str__(self):
       return "{}({})".format(self.name,self.descricao)

class Atividade(models.Model):
       numero = models.BigIntegerField(verbose_name="número")
       descricao = models.CharField(max_length=150, verbose_name="Descrição")
       pontos = models.DecimalField(decimal_places=1,max_digits=4)
       detalhes = models.CharField(max_length=100)

       campo = models.ForeignKey(Campo, on_delete=models.PROTECT)# proteção para não apagar os dados que estao em atividade
def __str__(self):
           return "{} {} ({})".format(self.nome, self.nivel, self.descricao)
class Classe(models.Model):
    nome = models.CharField(max_length=50, verbose_name="classe")
    descricao = models.CharField(max_length=150, verbose_name="Descrição", null=True, blank=True)
    nivel = models.IntegerField(verbose_name="nivel")

class Progressao(models.Model):
    servidor = models.CharField(max_length=255)  # Assumindo que este campo está correto
    classe = models.CharField(max_length=255)   # Assumindo que este campo está correto
    data_inicial = models.DateField()
    data_final = models.DateField(null=True, blank=True)
    observacao = models.CharField(max_length=255, verbose_name="Observação")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} -> {} | {} a {}".format(self.servidor, self.classe, self.data_inicial, self.data_final)
class Comprovante(models.Model):
    progresso = models.ForeignKey(Progressao, on_delete=models.PROTECT, verbose_name="progressao" )
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    quantidade = models.DecimalField(decimal_places=2, max_digits=5)
    data = models.DateField()
    data_final = models.DateField(null=True, blank=True, help_text="informe apenas se o comprovante for relativo a um periodo.")
    arquivo = models.FileField(upload_to=user_path)

    def _str_(self):
        return "[{}]{} - {}/{}".format(self.pk, self.servidor, self.progressao, self.atividade)