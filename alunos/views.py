from django.shortcuts import render, redirect, get_object_or_404
from .models import alunos

def show_home(request):
    return render(request, 'index.html')

def add_aluno(request):
        if request.method == 'POST':
            aluno_id = request.POST['aluno_id']
            nome = request.POST['nome']
            sobrenome = request.POST['sobrenome']
            idade = request.POST['idade']
            dataNascimento = request.POST['dataNascimento']
            dataIngresso = request.POST['dataIngresso']
            curso = request.POST['curso']
            
            if aluno_id:
                 aluno = aluno_id
                 aluno.nome = nome
                 aluno.sobrenome = sobrenome
                 aluno.idade = idade
                 aluno.dataNascimento = dataNascimento
                 aluno.dataIngresso = dataIngresso
                 aluno.curso = curso
                 aluno.save()
            else:
                 alunos.objects.create(
                    nome = nome,
                    sobrenome = sobrenome,
                    idade = idade,
                    dataNascimento = dataNascimento,
                    dataIngresso = dataIngresso,
                    curso = curso
                 )

            return redirect('add_aluno')
        allAlunos = alunos.objects.all()
        return render(request, 'index.html', {'alunos' : allAlunos})

def del_aluno(request, aluno_id):
    if request.method == "POST":
          aluno = get_object_or_404(alunos, id=aluno_id)
          aluno.delete()
    return redirect("add_aluno")
