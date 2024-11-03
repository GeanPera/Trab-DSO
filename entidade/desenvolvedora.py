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
