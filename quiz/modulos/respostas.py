class Respostas:

    # Lista onde as respostas que o usuário responder irão ficar armazenadas
    respostas_usuario = []
    # Lista de quantas vezes cada opção foi escolhida como resposta
    respostas_qtd = []

    def __init__(self):
        # Lista de respostas que estarão disponiveis para o usuário responder
        self.lista_de_respostas = []
        self.respostas_qtd = []