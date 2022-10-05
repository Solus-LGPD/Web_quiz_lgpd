from django.db import models


# Classe que será utilizada como objeto de configuração no banco de dados
class Cadastro(models.Model):

    # Metodo para ao vizualisar o banco de dados seja mostrado cada dado com o atributo nome
    def __str__(self) -> None:
        return self.nome_empresa

    nome_empresa = models.CharField(max_length=100, blank=False, null=False)
    nome_colaborador = models.CharField(max_length=100, blank=False, null=False)
    email_colaborador = models.EmailField(max_length=100, unique=True)
    whatsapp_colaborador = models.CharField(max_length=25, unique=True)
    senha = models.CharField(max_length=30, blank=False, null=False)
    termo_de_uso = models.BooleanField('Eu aceito os termos de uso', default=False)


class Pergunta(models.Model):

    def __str__(self) -> str:
        return self.pergunta

    pergunta = models.CharField(max_length=300, unique=True)
    pesos = models.FloatField(default=False, null=False)
    

class OpcaoResposta(models.Model):

    def __str__(self) -> str:
        return self.respostas

    respostas = models.CharField(max_length=200, unique=True)


class Questao(models.Model):

    def __str__(self) -> str:
        return str(self.data_de_envio) + '  -->  ' + str(self.empresa)

    resposta = models.CharField(max_length=1, default=None, null=True)
    data_de_envio = models.DateTimeField('data de envio', null=True, blank=True)
    empresa = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    opcao_resposta = models.ForeignKey(OpcaoResposta, on_delete=models.DO_NOTHING)

