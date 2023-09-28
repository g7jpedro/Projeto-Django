from django.shortcuts import render
from receitas.models import Receita, Categoria


def home(request):
    context = {
        'receitas': Receita.objects.filter(publicado=True)
    }
    
    return render(request, 'receitas/paginas/home.html', context)


def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    receitas = Receita.objects.filter(categoria=categoria, publicado=True).order_by('-id')

    context = {
        'receitas': receitas,
        'titulo': f'{categoria.categoria}'
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
