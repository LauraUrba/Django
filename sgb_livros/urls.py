from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    
    #path('livros/', views.livros, name='livros'),
    #path('salva_livros/', views.salvar_livro, name='salva_livros'),

    path('', views.cadastro_livro, name='cadastro_livro'),
]
