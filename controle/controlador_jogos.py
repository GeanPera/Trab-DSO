from limite.tela_loja import TelaLoja
from entidade.jogo import Jogo
from exceptions.campo_vazio_exception import CamposVaziosError


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
        try:
            genero = self.__tela.solicitar_genero()
            if not genero:
                raise CamposVaziosError
            
            jogos_gen = [jogo for jogo in self.__jogos if jogo.genero == genero]
            if jogos_gen:
                self.__tela.mostra_mensagem("Jogos no gênero selecionado:")
                for jogo in jogos_gen:
                    self.__tela.mostra_mensagem(f"- {jogo.titulo} R$: {jogo.preco}")
        except CamposVaziosError as e:
            self.__tela.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def jogos_por_desenvolvedora(self):
        try:
            desenvolvedora = self.__tela.solicitar_desenvolvedora()
            if not desenvolvedora:
                raise CamposVaziosError
            
            jogos_por_dev = [jogo for jogo in self.__jogos if jogo.desenvolvedora == desenvolvedora]
            if jogos_por_dev:
                self.__tela.mostra_mensagem("Jogos da desenvolvedora selecionada:")
                for jogo in jogos_por_dev:
                    self.__tela.mostra_mensagem(f"- {jogo.titulo} R$: {jogo.preco}")
            else:
                self.__tela.mostra_mensagem("Nenhum jogo encontrado para a desenvolvedora informada.")
        except CamposVaziosError as e:
            self.__tela.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def jogos_por_preco(self):
        try:
            preco_min, preco_max = self.__tela.solicitar_faixa_preco()
            preco_min = float(preco_min)
            preco_max = float(preco_max)
            if not preco_min or not preco_max:
                raise CamposVaziosError

            jogos_preco = [jogo for jogo in self.__jogos if preco_min <= jogo.preco <= preco_max]
            if jogos_preco:
                self.__tela.mostra_mensagem("Jogos dentro da faixa de preço selecionada:")
                for jogo in jogos_preco:
                    self.__tela.mostra_mensagem(f"- {jogo.titulo} (R$: {jogo.preco})")
            else:
                self.__tela.mostra_mensagem("Nenhum jogo encontrado nessa faixa de preço.")
        except CamposVaziosError as e:
            self.__tela.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela.mostra_mensagem(f"Erro inesperado: {str(e)}")

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

    def relatorio_vendas_por_jogo(self):
        relatorios = []
        jogos_por_desenvolvedora = {}
        for jogo in self.__jogos:
            desenvolvedora = jogo.desenvolvedora
            if desenvolvedora not in jogos_por_desenvolvedora:
                jogos_por_desenvolvedora[desenvolvedora] = []
            jogos_por_desenvolvedora[desenvolvedora].append(jogo)

        for desenvolvedora, jogos in jogos_por_desenvolvedora.items():
            receita_dev = 0
            relatorios.append(f"\nDesenvolvedora: {desenvolvedora}")
            for jogo in jogos:
                receita_jogo = jogo.preco * jogo.qntd_vendida
                receita_dev += receita_jogo
                relatorios.append(f"Título: {jogo.titulo}, Quantidade Vendida: {jogo.qntd_vendida}, Preço: {jogo.preco}, Receita do Jogo: {receita_jogo}")
            relatorios.append(f"Receita Total da Desenvolvedora: {receita_dev}")

        return relatorios

    def relatorio_jogos_por_faixa_etaria(self):
        relatorios = []
        jogos_por_faixa = {}
        for jogo in self.__jogos:
            faixa = jogo.faixa_etaria
            if faixa not in jogos_por_faixa:
                jogos_por_faixa[faixa] = []
            jogos_por_faixa[faixa].append(jogo)

        for faixa, jogos in jogos_por_faixa.items():
            relatorios.append(f"\nFaixa Etária: {faixa}+")
            for jogo in jogos:
                relatorios.append(f"Título: {jogo.titulo}, Gênero: {jogo.genero}, Desenvolvedora: {jogo.desenvolvedora}")
        return relatorios

    def relatorio_generos_populares(self):
        relatorios = []
        generos = {}
        for jogo in self.__jogos:
            genero = jogo.genero
            generos[genero] = generos.get(genero, 0) + jogo.qntd_vendida

        for genero, total_vendas in generos.items():
            relatorios.append(f"Gênero: {genero}, Quantidade Total Vendida: {total_vendas}")
        return relatorios

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
