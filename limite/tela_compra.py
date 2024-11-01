class TelaCompra:
    def opcao_compra(self):
        print("--- Opção de Compra ---")
        print("1 - Comprar")
        print("2 - Presentear")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))
        return opcao

    def pede_nickname(self, mensagem):
        return input(mensagem)

    def solicitar_jogo(self, mensagem):
        return input(mensagem)

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")
