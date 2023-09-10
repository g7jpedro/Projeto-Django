from django.shortcuts import render
from receitas.models import Receita


def home(request):

    context = {
        'receitas': Receita.objects.all() 
    }
    return render(request, 'receitas/paginas/home.html', context)


def receitas(request, id):
    return render(request, 'receitas/paginas/receitas-view.html', context= { 
        'is_detail_page': True,
        'receita_imagem': True, 
    })
