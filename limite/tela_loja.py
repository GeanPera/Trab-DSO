class TelaLoja:
    def exibir_menu(self):
        print("--- Menu da Loja ---")
        print("1 - Todos os jogos")
        print("2 - Jogo mais comprado")
        print("3 - Jogos por gênero")
        print("4 - Jogos por desenvolvedora")
        print("5 - Filtrar por preço")
        print("0 - Retornar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

<<<<<<< HEAD
    def mostrar_jogo_mais_comprado(self, jogo):
        if jogo:
            print(f"O jogo mais comprado é: {jogo.titulo} com {jogo.qntd_vendida} vendas.")
        else:
            print("Nenhum jogo disponível.")

    #Aqui dá pra fazer o método mostrar a lista de gêneros disponíveis
    def mostrar_jogos_por_genero(self, jogos):
        if jogos:
            print("Jogos no gênero selecionado:")
            for jogo in jogos:
                print(f"- {jogo.titulo}")
        else:
            print("Nenhum jogo encontrado no gênero informado.")

    def mostrar_jogos_por_desenvolvedora(self, jogos):
        if jogos:
            print("\nJogos da desenvolvedora selecionada:")
            for jogo in jogos:
                print(f"- {jogo.titulo}")
        else:
            print("Nenhum jogo encontrado para a desenvolvedora informada.")

    def filtrar_jogos_por_preco(self, jogos):
        if jogos:
            print("\nJogos dentro da faixa de preço selecionada:")
            for jogo in jogos:
                print(f"- {jogo.titulo} ({jogo.preco} reais)")
        else:
            print("Nenhum jogo encontrado nessa faixa de preço.")
=======
    def opcao_compra(self):
        print("--- Opção de Compra ---")
        print("1 - Comprar")
        print("2 - Presentear")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def solicitar_jogo(self, mensagem):
        return input(mensagem)
>>>>>>> 210f136eaae04ddd2a5f7cfc054577d1372c387b

    def solicitar_genero(self):
        return input("Digite o gênero desejado: ")

    def solicitar_desenvolvedora(self):
        return input("Digite a desenvolvedora desejada: ")

    def solicitar_faixa_preco(self):
        preco_min = float(input("Digite o preço mínimo: "))
        preco_max = float(input("Digite o preço máximo: "))
        return preco_min, preco_max

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")