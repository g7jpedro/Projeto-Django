from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=100)

class Receita(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    descricao = models.CharField('Descrição', max_length=160)
    models.SlugField()
    tempo_preparacao = models.IntegerField('Tempo de preparação')
    tempo_preparacao_unidade = models.CharField('Tempo preparação unidade', max_length=65)
    porcoes = models.IntegerField('Porções')
    porcoes_unidade = models.CharField('Porções Unidade', max_length=65)
    preparacao =  models.TextField('Preparação')
    preparacao_is_html = models.BooleanField('Preparação is hmtl', default=False)
    criacao = models.DateTimeField('Criação', auto_now_add=True)
    modificacao = models.DateTimeField('Modificação', auto_now=True)
    is_publicado = models.BooleanField('Públicado ?', default=False)
    imagem = models.ImageField(upload_to='receitas/imagens/%Y/%m/%d/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    
    def __str__(self):
        return self.titulo[:10]
