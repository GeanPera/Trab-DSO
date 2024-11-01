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

    def opcao_compra(self):
        print("--- Opção de Compra ---")
        print("1 - Comprar")
        print("2 - Presentear")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def solicitar_jogo(self, mensagem):
        return input(mensagem)

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