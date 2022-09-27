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

        self.__estrelas = 10 * self.__pontuacao_parcial# Calculo das estrelas

    # Função utilizada para calcular a pontuação parcial do usuário (100% = 2 pontos, 50% = 1 ponto)
    def calculo_pontuacao_parcial(self, lista_respostas) -> None:
        """
            -> Função utilizada para calcular a pontuação parcial do usuário no teste de adequação
        :return: Não retorna nada
        """
        # Esse for anda pela lista respostas_qtd e também pelo seu indice
        # a variável [c] significa o valor da resposta dada ao Quiz
        for pos, c in enumerate(lista_respostas):  
            if c == 0: 
                self.__pontuacao_parcial += 0
            elif c == 1:
                if self.perguntas_pesos.get(id=pos+1).pesos == 0.05:
                    self.__pontuacao_parcial += 0.05 * 0.25 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.1:
                    self.__pontuacao_parcial += 0.1 * 0.25 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.15:
                    self.__pontuacao_parcial += 0.15 * 0.25 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.2:
                    self.__pontuacao_parcial += 0.2 * 0.25
            elif c == 2:
                if self.perguntas_pesos.get(id=pos+1).pesos == 0.05:
                    self.__pontuacao_parcial += 0.05 * 0.5 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.1:
                    self.__pontuacao_parcial += 0.1 * 0.5 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.15:
                    self.__pontuacao_parcial += 0.15 * 0.5 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.2:
                    self.__pontuacao_parcial += 0.2 * 0.5 
            elif c == 3:
                if self.perguntas_pesos.get(id=pos+1).pesos == 0.05:
                    self.__pontuacao_parcial += 0.05 * 1 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.1:
                    self.__pontuacao_parcial += 0.1 * 1 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.15:
                    self.__pontuacao_parcial += 0.15 * 1 
                elif self.perguntas_pesos.get(id=pos+1).pesos == 0.2:
                    self.__pontuacao_parcial += 0.2 * 1 
    
    
    def get_estrelas(self):
        return self.__estrelas

    # Retorna o valor da pontuação parcial
    def get_pontuacao_parcial(self):
        return self.__pontuacao_parcial


