class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Tela Sistemas ---------")
        print("Escolha sua opcao")
        print("1 - Menu da Loja")
        print("2 - Usuário")
        opcao = int(input("Escolha a opcao:"))
        return opcao