from django.urls import path
from receitas.views import home, categoria

app_name = 'receitas'

urlpatterns = [
    path('', home, name='home'),
    path('receitas/categoria/<int:categoria_id>/', categoria, name='categoria'),
    #path('receitas/<int:id>/', receitas, name='receita'),
]
