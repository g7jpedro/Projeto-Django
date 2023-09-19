from django.urls import path
from receitas.views import home, categoria, autor

app_name = 'receitas'

urlpatterns = [
    path('', home, name='home'),
    path('receitas/categoria/<int:categoria_id>/', categoria, name='categoria'),
    path('receitas/autor/<int:autor_id>/', autor, name='autor'),
    #path('receitas/<int:id>/', receitas, name='receita'),
]
