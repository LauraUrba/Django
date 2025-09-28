from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def cadastra_usuario(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome_usuario = request.POST['nome_usuario']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']

        # Verifica se o usuário já existe
        usuario_existente = User.objects.filter(username=nome_usuario).first()
        
        if usuario_existente:
            return HttpResponse('Usuário já existe!')
        else:
            usuario = User.objects.create_user(
                username=nome_usuario,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            usuario.save()
            return HttpResponse('Usuário cadastrado com sucesso!')

