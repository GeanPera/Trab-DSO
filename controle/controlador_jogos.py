from limite.tela_loja import TelaLoja
from entidade.jogo import Jogo

class ControladorJogos:
    def __init__(self, controlador_sistema):
        self.__jogos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaLoja()

    def novo_jogo(self, titulo, genero, desenvolvedora, faixa_etaria, descricao, preco, qnt_vendida):
        jogo = Jogo(titulo, genero, desenvolvedora, faixa_etaria, descricao, preco, qnt_vendida)
        self.__jogos.append(jogo)

    def jogo_mais_comprado(self):
        if not self.__jogos:
            return None
        return max(self.__jogos, key=lambda jogo: jogo.qnt_vendida)

    def jogos_por_genero(self, genero):
        return [jogo for jogo in self.__jogos if jogo.genero == genero]

    def jogos_por_desenvolvedora(self, desenvolvedora):
        return [jogo for jogo in self.__jogos if jogo.desenvolvedora == desenvolvedora]

    def filtrar_preco(self, preco_minimo, preco_maximo):
        return [jogo for jogo in self.__jogos if preco_minimo <= jogo.preco <= preco_maximo]

    def abre_tela(self):
        while True:
            opcao = self.__tela.exibir_menu()

            if opcao == '1':
                jogo = self.jogo_mais_comprado()
                self.__tela.mostrar_jogo_mais_comprado(jogo)

            elif opcao == '2':
                genero = self.__tela.solicitar_genero()
                jogos = self.jogos_por_genero(genero)
                self.__tela.mostrar_jogos_por_genero(jogos)

            elif opcao == '3':
                desenvolvedora = self.__tela.solicitar_desenvolvedora()
                jogos = self.jogos_por_desenvolvedora(desenvolvedora)
                self.__tela.mostrar_jogos_por_desenvolvedora(jogos)

            elif opcao == '4':
                preco_min, preco_max = self.__tela.solicitar_faixa_preco()
                jogos = self.filtrar_preco(preco_min, preco_max)
                self.__tela.filtrar_jogos_por_preco(jogos)

            elif opcao == '0':
                print("Saindo da loja.")
                
                break

            else:
                print("Opção inválida. Tente novamente.")
