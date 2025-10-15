from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

LISTA_CATEGORIA = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    # Usa o nome do Título no painel administrativo ao invés do objeto
    def __str__(self):
        return self.titulo

# criar os episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    # Usa o nome do Título no painel administrativo ao invés do objeto
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

# criar os usuarios
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")
