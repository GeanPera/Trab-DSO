from limite.tela_loja import TelaLoja
from entidade.jogo import Jogo
from exceptions.campo_vazio_exception import CamposVaziosError


class ControladorJogos:
    def __init__(self, controlador_sistema):
        self.__jogos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaLoja()

    def novo_jogo(self, titulo, genero, desenvolvedora, faixa_etaria, descricao, preco, qnt_vendida, imagem):
        jogo = Jogo(titulo, genero, desenvolvedora, faixa_etaria, descricao, preco, qnt_vendida, imagem)
        self.__jogos.append(jogo)

    def listar_jogos(self):
        lista_jogos = []
        for jogo in self.__jogos:
            lista_jogos.append({'nome': jogo.titulo, 'preco': jogo.preco, 'imagem': jogo.imagem})
        mensagem = "Todos os Jogos:"
        self.exibir_comprar(mensagem, lista_jogos)

    def jogo_mais_comprado(self):
    # Ordena a lista de jogos por quantidade de vendas usando Bubble Sort
        lista_jogos = []
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
            lista_jogos.append({'nome': jogo.titulo, 'preco': f"{jogo.qntd_vendida} vendas.", 'imagem': jogo.imagem})
        else:
            self.__tela.mostra_mensagem("Nenhum jogo disponível.")
        mensagem = "Jogo mais comprado:"
        self.exibir_comprar(mensagem, lista_jogos)

    def jogos_por_genero(self):
        lista_jogos = []
        generos = self.generos()

        genero = self.__tela.solicitar_genero(generos)
        if genero != None:
            jogos_gen = [jogo for jogo in self.__jogos if jogo.genero == genero]
            if jogos_gen:
                for jogo in jogos_gen:
                    lista_jogos.append({'nome': jogo.titulo, 'preco': jogo.preco, 'imagem': jogo.imagem})
                mensagem = "Jogos no gênero selecionado:"
                self.exibir_comprar(mensagem, lista_jogos)
        else:
            return None

    def generos(self):
        generos = []
        for jogo in self.__jogos:
            if jogo.genero not in generos:
                generos.append(jogo.genero)
        return generos

    def jogos_por_desenvolvedora(self):
        lista_jogos = []
        desenvolvedoras = self.desenvolvedoras()

        desenvolvedora = self.__tela.solicitar_desenvolvedora(desenvolvedoras)
        if desenvolvedora != None:
            jogos_por_dev = [jogo for jogo in self.__jogos if jogo.desenvolvedora == desenvolvedora]
            if jogos_por_dev:
                for jogo in jogos_por_dev:
                    lista_jogos.append({'nome': jogo.titulo, 'preco': jogo.preco, 'imagem': jogo.imagem})
                mensagem = "Jogos da desenvolvedora selecionada:"
                self.exibir_comprar(mensagem, lista_jogos)
        else:
            return None

    def desenvolvedoras(self):
        desenvolvedoras = []
        for jogo in self.__jogos:
            if jogo.desenvolvedora not in desenvolvedoras:
                desenvolvedoras.append(jogo.desenvolvedora)
        return desenvolvedoras

    def jogos_por_preco(self):
        lista_jogos = []
        try:
            preco_min, preco_max = self.__tela.solicitar_faixa_preco()
            if preco_min != None:
                preco_min = float(preco_min)
                preco_max = float(preco_max)
                if not preco_min or not preco_max:
                    raise CamposVaziosError

                jogos_preco = [jogo for jogo in self.__jogos if preco_min <= jogo.preco <= preco_max]
                if jogos_preco:
                    for jogo in jogos_preco:
                        lista_jogos.append({'nome': jogo.titulo, 'preco': jogo.preco, 'imagem': jogo.imagem})
                    mensagem = "Jogos dentro da faixa de preço selecionada:"
                    self.exibir_comprar(mensagem, lista_jogos)
                else:
                    self.__tela.mostra_mensagem("Nenhum jogo encontrado nessa faixa de preço.")
        except CamposVaziosError as e:
            self.__tela.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def exibir_comprar(self, mensagem, lista_jogos):
        jogo = self.__tela.exibir_lista_jogos(mensagem, lista_jogos)
        if jogo == '-Retornar-':
            return
        else:
            self.__controlador_sistema.controlador_compra.abre_tela(jogo)
    def retornar_inicio(self):
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
            relatorios.append(f"Desenvolvedora: {desenvolvedora}")
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

            funcao_menu = opcoes_menu[opcao_menu]
            funcao_menu()
            if opcao_menu == 0:
                break

