from django.shortcuts import render
from .models import Cadastro, Questao, Pergunta, OpcaoResposta
from .modulos.login import Login
from .forms import CadastroForm
from .modulos.login import Login
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .modulos.respostas import Respostas
from .modulos.pontuacoes import Pontuacoes
from datetime import datetime
from django.utils import timezone


def index(request):
    return render(request, 'quiz/index.html')


def quiz(request, id_usuario):
    context = {}
    pont = Pontuacoes()

    if request.method == 'POST':
        lista_respostas = []
        for v in range(1, 8):
            resposta = (int(request.POST.get(f'stp_{v}_valor_selecao', None)))
            lista_respostas.append(resposta)
            q = Questao(data_de_envio=datetime.now(), resposta=resposta, empresa=Cadastro.objects.get(pk=id_usuario), pergunta=Pergunta.objects.get(pk=v), opcao_resposta=OpcaoResposta.objects.get(pk=resposta + 1))
            q.save()
        
        
        pont.calculo_pontuacao_parcial(lista_respostas)  
        pont.calculo_estrela()
        print(lista_respostas)  
        # retorna valores filtrando p = Questao.objects.filter(empresa=Cadastro.objects.get(id=id_usuario), data_de_envio=datetime.now())

        context = {
            'estrelas': round(pont.get_estrelas(),2)
        }

        return render(request, 'quiz/resultado.html', context)

    return render(request, 'quiz/quiz.html')

def resultado(request):
    return render(request, 'quiz/resultado.html')


def login(request):
    fail = 0
    context = {
        'fail': fail
    }
    perguntas = Pergunta.objects.all()


    if request.method == 'POST':

        log = Login()

        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)

        if log.verificarLogin(email, senha) != 0:
            context = {
                'id_usuario': log.verificarLogin(email, senha),
                'perguntas': perguntas,
                'fail' : fail
            }
            return render(request, 'quiz/quiz.html', context)
        else:
            fail = 1
            context = {
                'fail' : fail
            }

    return render(request, 'quiz/login_register.html', context)


def cadastro(request):
    human = 3
    password_token = 3

    if request.POST:
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form.data['senha'] == form.data['confirmar_senha']:
                cliente = form.save()
                form = CadastroForm()
                human = 1
                password_token = 1
            else:
                password_token = 0
        else:
            human = 0
    else:
        form = CadastroForm()

    context = {
    'form': form,
    'human': human,
    'ps_token' : password_token
    }

    return render(request, 'quiz/cadastro.html', context)


def termo(request):
    return render(request, 'quiz/termo.html')

