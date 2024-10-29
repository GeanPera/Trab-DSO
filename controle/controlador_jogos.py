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
# Ordena a lista de jogos por quantidade de vendas usando Bubble Sort
        jogos_ordenados = self.__jogos
        n = len(jogos_ordenados)
        
        for i in range(n - 1):
            for j in range(n - i - 1):
                if jogos_ordenados[j].qntd_vendida < jogos_ordenados[j + 1].qntd_vendida:
                    # Troca os jogos de posição se o atual tiver menos vendas que o próximo
                    jogos_ordenados[j], jogos_ordenados[j + 1] = jogos_ordenados[j + 1], jogos_ordenados[j]
        
        # Retorna o primeiro jogo da lista ordenada (com a maior quantidade de vendas)
        return jogos_ordenados[0] if jogos_ordenados else None

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
                jogo_mais = self.jogo_mais_comprado()
                self.__tela.mostrar_jogo_mais_comprado(jogo_mais)

            elif opcao == '2':
                genero = self.__tela.solicitar_genero()
                jogos_gen = self.jogos_por_genero(genero)
                self.__tela.mostrar_jogos_por_genero(jogos_gen)

            elif opcao == '3':
                desenvolvedora = self.__tela.solicitar_desenvolvedora()
                jogos_dev = self.jogos_por_desenvolvedora(desenvolvedora)
                self.__tela.mostrar_jogos_por_desenvolvedora(jogos_dev)

            elif opcao == '4':
                preco_min, preco_max = self.__tela.solicitar_faixa_preco()
                jogos_preco = self.filtrar_preco(preco_min, preco_max)
                self.__tela.filtrar_jogos_por_preco(jogos_preco)

            elif opcao == '0':
                print("Saindo da loja.")
                
                break

            else:
                print("Opção inválida. Tente novamente.")
