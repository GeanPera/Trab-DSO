import random


class Biblioteca():
    def __init__(self):
        self.__jogos = []

    @property
    def jogos(self):
        return self.__jogos

    def adicionar_jogo(self, jogo):
        adiciona = True
        for game in self.__jogos:
            if game == jogo:
                adiciona = False
                return adiciona
        if adiciona:
            self.__jogos.append(jogo)
            return True

    def remover_jogo(self, jogo):
        self.__jogos.remove(jogo)
        print(f"Você removeu o jogo {jogo.titulo} da sua biblioteca!")

    def jogar(self, Jogo):
        pontuacao = random.randint(100, 10000)
        return print(f"Você jogou {Jogo.titulo}! Sua pontuação foi {pontuacao}")

    def jogar_junto(self, Jogo, Usuario):
        resultado = random.randint(0, 1)
        if resultado == 0:
            return print(f"Você ganhou uma partida de {Jogo.titulo} contra {Usuario.nickname}")
        else:
            return print(f"Você perdeu uma partida de {Jogo.titulo} contra {Usuario.nickname}")

    def mostrar_biblioteca(self):
        return [jogo.titulo for jogo in self.__jogos]