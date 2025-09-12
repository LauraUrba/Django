from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Livro
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


def cadastro_livro(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        ano_publicacao = request.POST['ano_publicacao']
        editora = request.POST['editora']
        if livro_id:  # Se o ID do livro for fornecido, atualize o livro existente. Ele edita
            livro = livro_id
            livro.titulo = titulo
            livro.autor = autor
            livro.ano_publicacao = ano_publicacao
            livro.editora = editora
            livro.save()
        else:  # Caso contrário, crie um novo livro. Ele cria
            Livro.objects.create(
                titulo = titulo,
                autor = autor,
                ano_publicacao = ano_publicacao,
                editora = editora
            )
        return redirect('cadastro_livro')
    # objects é um gerenciador de modelos padrão do Django que permite interagir/consultar com o banco de dados
    # all é uma função que recupera todos os registros da tabela livro - é o select do BD
    livros = Livro.objects.all()  # Recupera todos os livros do banco de dados
    return render(request, 'livros.html', {'livros': livros})
