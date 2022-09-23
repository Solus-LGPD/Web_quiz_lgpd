from ..models import Pergunta, Questao

class Pontuacoes:

    __estrelas = 0
    __pontuacao_parcial = 0
    
    def __init__(self) -> None:
        self.questao = Questao.objects.all()
        self.perguntas_pesos = Pergunta.objects.all()

    # Função utilizada para calcular a quantidade de estrelas que o usuário vai receber
    def calculo_estrela(self) -> None:
        """
            -> Função utilizada para calcular a quantidade de estrelas baseada no teste de adequação a LPGD.
        :return: Não retorna nada.
        """
        numero_de_perguntas = 8

        self.__estrelas = (5 * self.__pontuacao_parcial) / numero_de_perguntas # Calculo das estrelas

    # Função utilizada para calcular a pontuação parcial do usuário (100% = 2 pontos, 50% = 1 ponto)
    def calculo_pontuacao_parcial(self, lista_respostas) -> None:
        """
            -> Função utilizada para calcular a pontuação parcial do usuário no teste de adequação
        :return: Não retorna nada
        """
        for pos, c in enumerate(lista_respostas):  # Esse for anda pela lista respostas_qtd e também pelo seu indice
            if c == 0: 
                if self.perguntas_pesos.get(id=pos+1).pesos == 1:
                    self.__pontuacao_parcial += 0
                else:
                    self.__pontuacao_parcial += 0
            elif c == 1:
                if self.perguntas_pesos.get(id=pos+1).pesos == 1:
                    self.__pontuacao_parcial += 0.25
                else:
                    self.__pontuacao_parcial += 0.50
            elif c == 2: 
                if self.perguntas_pesos.get(id=pos+1).pesos == 1:
                    self.__pontuacao_parcial += 0.50
                else:
                    self.__pontuacao_parcial += 1
            elif c == 3:
                if self.perguntas_pesos.get(id=pos+1).pesos == 1:
                    self.__pontuacao_parcial += 1
                else:
                    self.__pontuacao_parcial += 2

    # Retorna o valor de estrelas
    def get_estrelas(self):
        return self.__estrelas

    # Retorna o valor da pontuação parcial
    def get_pontuacao_parcial(self):
        return self.__pontuacao_parcial


