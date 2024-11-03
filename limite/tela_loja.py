class TelaLoja:
    def exibir_menu(self):
        while True:
            print("--- Menu da Loja ---")
            print("1 - Todos os jogos")
            print("2 - Jogo mais comprado")
            print("3 - Jogos por gênero")
            print("4 - Jogos por desenvolvedora")
            print("5 - Filtrar por preço")
            print("0 - Retornar")
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Por favor, insira um número correspondente à opção.")

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