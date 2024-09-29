from pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome, email, nickname, idade, endereco, senha, cpf):
        super.__init__(nome, email, nickname, idade)
        self.__endereco = endereco
        self.__senha = senha
        self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def cpf(self):
        return self.__senha

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
