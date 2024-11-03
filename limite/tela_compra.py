class TelaCompra:
    def opcao_compra(self):
        while True:
            print("--- Opção de Compra ---")
            print("1 - Comprar")
            print("2 - Presentear")
            print("0 - Voltar")
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Por favor, insira um número correspondente à opção.")

    def pede_nickname(self, mensagem):
        return input(mensagem)

    def solicitar_jogo(self, mensagem):
        return input(mensagem)

    def pede_senha(self):
        senha = input("Insira sua senha: ")
        return senha

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")
