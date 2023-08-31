from django.contrib import admin
from receitas.models import Categoria, Receita

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...
    

