class TelaLoja:
    def exibir_menu(self):
        print("--- Menu da Loja ---")
        print("1 - Jogo mais comprado")
        print("2 - Jogos por gênero")
        print("3 - Jogos por desenvolvedora")
        print("4 - Filtrar por preço")
        print("0 - Retornar")
        opcao = input("Escolha uma opção: ")
        return opcao

    def mostrar_jogo_mais_comprado(self, jogo):
        
        if jogo:
            print(f"O jogo mais comprado é: {jogo.titulo} com {jogo.qntd_vendida} vendas.")
        else:
            print("Nenhum jogo disponível.")

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

    def solicitar_genero(self):
        return input("Digite o gênero desejado: ")

    def solicitar_desenvolvedora(self):
        return input("Digite a desenvolvedora desejada: ")

    def solicitar_faixa_preco(self):
        preco_min = float(input("Digite o preço mínimo: "))
        preco_max = float(input("Digite o preço máximo: "))
        return preco_min, preco_max
