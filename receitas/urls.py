from django.urls import path
from receitas.views import home, receitas

app_name = 'receitas'

urlpatterns = [
    path('', home, name='home'),
    path('receitas/<int:id>/', receitas, name='receita'),
]
