from django.urls import path
from receitas.views import home, receitas


urlpatterns = [
    path('', home),
    path('receitas/<int:id>/', receitas),
]
