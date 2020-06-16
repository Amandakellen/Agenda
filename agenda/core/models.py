from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo=models.CharField(max_length=100)
    descricao=models.TextField(blank=True,null=True)#Pode ser em branco e pode ser nulo
    data_evento=models.DateTimeField(verbose_name='Data do Evento')
    data_criacao=models.DateTimeField(auto_now=True)#insere data atual quando o registro é criado
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='evento'
        #para criar uma tabela com o nome que eu escolher,se não coloco isso
        #ele cria automaticamente com o nome core_evento

    def __str__(self):
      return self.titulo