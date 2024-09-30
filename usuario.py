from pessoa import Pessoa
from perfil import Perfil
from biblioteca import Biblioteca


class Usuario(Pessoa):

    def __init__(self, nome, nickname, idade, email: str, endereco: str, senha: str, cpf: str, saldo=0):
        super().__init__(nome, nickname, idade)
        self.__email = email
        self.__endereco = endereco
        self.__senha = senha
        self.__cpf = cpf
        self.__saldo = 0
        self.perfil = Perfil(nome, nickname, idade, saldo)
        self.biblioteca = Biblioteca()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

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
        return self.__cpf
