
class TelaUsuario():
    def opcoes_tela(self):
        print("-------- Tela Usuario ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Adicionar Amigo")
        print("5 - Excluir Amigo")
        print("6 - Depositar Saldo")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def dados_usuario():
       print("-----DADOS USUÁRIO-----")
       nome = input("Nome: ")
       nickname = input("Nickname: ")
       idade = int(input("Idade: "))
       email = input("E-mail: ")
       endereco = input("Endereço: ")
       senha = input("Senha: ")
       cpf = input("CPF: ")
       

    def alterar_usuario():
        pass
