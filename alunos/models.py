from django.db import models

class alunos(models.Model):
        nome = models.CharField(max_length=200)
        sobrenome = models.CharField(max_length=25)
        idade = models.IntegerField(max_length=3)
        dataNascimento = models.DateField()
        dataIngresso = models.DateField()
        curso = models.CharField(max_length=50)
