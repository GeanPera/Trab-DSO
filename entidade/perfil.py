
class Perfil():

    def __init__(self, nome, nickname, idade, saldo):
        self.__nome = nome
        self.__nickname = nickname
        self.__idade = idade
        self.__saldo = saldo
        self.__amigos = []
        self.__jogos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        self.__nickname = nickname

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
            self.__idade = idade

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):

        self.__saldo = saldo
