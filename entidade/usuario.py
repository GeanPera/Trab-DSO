from entidade.pessoa import Pessoa
from entidade.perfil import Perfil
#from entidade.biblioteca import Biblioteca


class Usuario(Pessoa):

    def __init__(self, nome, nickname, idade, email: str, endereco: str, senha: str, cpf: str, saldo=0):
        super().__init__(nome, nickname, idade)
        self.__email = email
        self.__endereco = endereco
        self.__senha = senha
        self.__cpf = cpf
        self.__saldo = 0
        self.__amigos = []
        self.__jogos = []

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

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def amigos(self):
        return self.__amigos

    @property
    def jogos(self):
        return self.__jogos
