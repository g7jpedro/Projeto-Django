from django.shortcuts import render


def home(request):
    return render(request, 'receitas/paginas/home.html')


def receitas(request, id):
    return render(request, 'receitas/paginas/receitas-view.html')
