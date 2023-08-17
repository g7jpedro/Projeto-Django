from django.urls import path
from receitas.views import home, contato, sobre


urlpatterns = [
    path('', home),
    path('contato', contato),
    path('sobre', sobre),
]