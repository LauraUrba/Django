from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def livros(request):
    return render(request, 'livros.html')

def salvar_livro(request):
    if request.method == 'POST':
        titulo_livro = request.POST['titulo_livro']
        autor_livro = request.POST['autor_livro']
        editora = request.POST['editora']
        return render(request, 'livros.html', context={
            'titulo_livro': titulo_livro,
            'autor_livro': autor_livro,
            'editora': editora
        })
    return HttpResponse('Método não permitido', status=405)

def index(request):
    return render(request, 'index.html')