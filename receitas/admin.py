from django.contrib import admin
from receitas.models import Categoria, Receita

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    

