class TelaSistema:
    def tela_opcoes(self):
        while True:
            print("-------- Tela Sistemas ---------")
            print("Escolha sua opcao")
            print("1 - Menu da Loja")
            print("2 - Usuário")
            print("3 - Relatório")
            print("0 - Sair")
            try:
                opcao = int(input("Escolha uma opção: "))
                return opcao
            except ValueError:
                self.mostra_mensagem("Entrada inválida! Por favor, insira um número correspondente à opção.")

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")