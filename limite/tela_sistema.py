class TelaSistema:
    def tela_opcoes(self):
        print("-------- Tela Sistemas ---------")
        print("Escolha sua opcao")
        print("1 - Menu da Loja")
        print("2 - Usuário")
        print("3 - Relatório")
        print("0 - Sair")
        opcao = int(input("Escolha a opcao:"))
        return opcao

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")