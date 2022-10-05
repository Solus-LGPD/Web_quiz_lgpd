from django.contrib import admin
from .models import Cadastro, Questao, Pergunta, OpcaoResposta


# Registra os modelos seguintes nas configurações de administração do Django.
admin.site.register(Cadastro)
admin.site.register(Questao)
admin.site.register(Pergunta)
admin.site.register(OpcaoResposta)
