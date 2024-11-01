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

    def listar_jogos(self):
        self.__tela.mostra_mensagem("Todos os jogos disponíveis:")
        for jogo in self.__jogos:
            self.__tela.mostra_mensagem(f"- {jogo.titulo} R$: {jogo.preco}")

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
        jogo = jogos_ordenados[0] if jogos_ordenados else None
        if jogo:
            mensagem = f"O jogo mais comprado é: {jogo.titulo} com {jogo.qntd_vendida} vendas."
        else:
            mensagem = "Nenhum jogo disponível."
        self.__tela.mostra_mensagem(mensagem)

    def jogos_por_genero(self):
        genero = self.__tela.solicitar_genero()
        jogos_gen = [jogo for jogo in self.__jogos if jogo.genero == genero]
        if jogos_gen:
            self.__tela.mostra_mensagem("Jogos no gênero selecionado:")
            for jogo in jogos_gen:
                self.__tela.mostra_mensagem(f"- {jogo.titulo} R$: {jogo.preco}")
        else:
            self.__tela.mostra_mensagem("Nenhum jogo encontrado no gênero informado.")

    def jogos_por_desenvolvedora(self):
        desenvolvedora = self.__tela.solicitar_desenvolvedora()
        jogos_por_dev = [jogo for jogo in self.__jogos if jogo.desenvolvedora == desenvolvedora]
        if jogos_por_dev:
            self.__tela.mostra_mensagem("Jogos da desenvolvedora selecionada:")
            for jogo in jogos_por_dev:
                self.__tela.mostra_mensagem(f"- {jogo.titulo} R$: {jogo.preco}")
        else:
            self.__tela.mostra_mensagem("Nenhum jogo encontrado para a desenvolvedora informada.")
        

    def jogos_por_preco(self):
        preco_min, preco_max = self.__tela.solicitar_faixa_preco()
        jogos_preco = [jogo for jogo in self.__jogos if preco_min <= jogo.preco <= preco_max]
        if jogos_preco:
            self.__tela.mostra_mensagem("Jogos dentro da faixa de preço selecionada:")
            for jogo in jogos_preco:
                self.__tela.mostra_mensagem(f"- {jogo.titulo} (R$: {jogo.preco})")
        else:
            self.__tela.mostra_mensagem("Nenhum jogo encontrado nessa faixa de preço.")

    def retornar_inicio(self):
        self.__tela.mostra_mensagem("Retornando...")
        return

    def jogo(self, nome_jogo):
        jogo_escolhido = None
        for jogo in self.__jogos:
            if jogo.titulo == nome_jogo:
                jogo_escolhido = jogo
                break
        return jogo_escolhido

    def abre_tela(self):
        opcoes_menu = {1: self.listar_jogos, 2: self.jogo_mais_comprado, 3: self.jogos_por_genero,
                        4: self.jogos_por_desenvolvedora, 5: self.jogos_por_preco, 0: self.retornar_inicio}
        while True:
            opcao_menu = self.__tela.exibir_menu()
            try:
                funcao_menu = opcoes_menu[opcao_menu]
                funcao_menu()
                if opcao_menu == 0:
                    break
                self.__controlador_sistema.controlador_compra.abre_tela()
            except KeyError:
                self.__tela.mostra_mensagem("Opção inválida. Tente novamente.")
