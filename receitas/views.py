from django.shortcuts import render
from receitas.models import Receita 


def home(request):
    context = {
        'receitas': Receita.objects.filter(publicado=True)
    }
    
    return render(request, 'receitas/paginas/home.html', context)


def categoria(request, categoria_id):
    context = {
        'receitas': Receita.objects.filter(categoria__id=categoria_id, publicado=True)
    }
    
    return render(request, 'receitas/paginas/categoria.html', context)


def autor(request, autor_id):
    context = {
        'receitas': Receita.objects.filter(autor__id=autor_id, publicado=True)
    }
    
    return render(request, 'receitas/paginas/autor.html', context)


def receitas(request, id):
    return render(request, 'receitas/paginas/receitas-view.html', context= { 
        'is_detail_page': True,
        'receita_imagem': True, 
    })
