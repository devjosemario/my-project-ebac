from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Habilidade(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Experiencia(models.Model):
    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"