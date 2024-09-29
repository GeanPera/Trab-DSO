from pessoa import Pessoa
from jogo import Jogo


class Amigo(Pessoa):
    def __init__(self, nome, email, nickname, idade, jogos: Jogo):
        super.__init__(nome, email, nickname, idade)
        self.__jogos = []

    def biblioteca_de_jogos(self):
        pass

    def jogatinas(self, Jogo):
        pass
