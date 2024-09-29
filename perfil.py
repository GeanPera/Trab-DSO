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


    def adicionar_amigo(self, Amigo):
        self.__amigos.append(Amigo)

    def remover_amigo(self, Amigo):
        self.__amigos.remove(Amigo)

    def depositar_saldo(self, valor):
        self.__saldo += valor
        print(f"Depósito realizado! Saldo atual do perfil: R${self.__saldo:.2f}")

    def descontar_saldo(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente para esta compra!")
            return False
        else:
            self.__saldo -= valor
            print(f"Compra efetuada com sucesso! Seu saldo atual é R${self.__saldo:.2f}")
            return True
