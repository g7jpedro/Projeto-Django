from django.db import models 
from django.contrib.auth.models import User


class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=100)

    def __str__(self):
        return self.categoria


class Receita(models.Model):
    titulo = models.CharField('Título', max_length=50)
    descricao = models.CharField('Descrição', max_length=200)
    preparacao = models.TextField('Preparação')
    tempo_preparacao = models.IntegerField('Tempo de preparação')
    tempo_tipo = models.CharField('Tipo de tempo', max_length=20)
    porcao = models.IntegerField('Porções')
    porcao_tipo = models.CharField('Tipo de porção', max_length=20)
    criacao = models.DateTimeField('Criação', auto_now_add=True)
    modificacao = models.DateTimeField('Modificação', auto_now=True)
    imagem = models.ImageField('Imagem', upload_to='receitas/imagem/%Y/%m/%d/')
    publicado = models.BooleanField('Públicado ?', default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField('Slug')

    def __str__(self):
        return self.titulo
