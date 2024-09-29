
class Perfil():
    def __init__(self, nome, nickname, idade, saldo):
        self.nome = nome
        self.nickname = nickname
        self.idade = idade
        self.__saldo = saldo
        self.__amigos = []

    @property
    def saldo(self):
        return self.__saldo

    def adicionar_amigo(self, Usuario):
        self.__amigos.append(Usuario)
        return print(f"Agora {Usuario.nickname} está na sua lista de amigos!")

    def remover_amigo(self, Usuario):
        self.__amigos.remove(Usuario)
        return print(f"Você removeu {Usuario.nickname} da sua lista de amigos!")

    def depositar_saldo(self, valor):
        self.__saldo += valor
        print(f"Depósito realizado! Saldo atual é R${self.__saldo:.2f}")

    def descontar_saldo(self, valor):
        if valor > self.__saldo:
            print(f"Saldo insuficiente para esta compra! Seu saldo atual é R${self.__saldo:.2f}")
            return False
        else:
            self.__saldo -= valor
            return True
