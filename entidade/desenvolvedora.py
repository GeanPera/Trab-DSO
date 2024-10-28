class Desenvolvedora:
    def __init__(self, nome):
        self.__nome = nome
        self.__jogos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def jogos(self):
        return self.__jogos

    def lancar_jogo(self, jogo):
        self.__jogos.append(jogo)

    def listar_jogos(self):
        return [jogo.titulo for jogo in self.__jogos]

    def faturamento(self):
        total_faturamento = sum(jogo.preco * jogo.qntd_vendida for jogo in self.__jogos)
        return f"R${total_faturamento:.2f}"
