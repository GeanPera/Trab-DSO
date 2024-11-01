class TelaUsuario():
    def opcoes_tela(self):
        print("-------- Tela Usuario ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Adicionar Amigo")
        print("4 - Excluir Amigo")
        print("5 - Depositar Saldo")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def dados_usuario(self):
        print("-----DADOS USUÁRIO-----")
        nome = input("Nome: ")
        nickname = input("Nickname: ")
        idade = int(input("Idade: "))
        email = input("E-mail: ")
        endereco = input("Endereço: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")

        return {"nome": nome, "nickname": nickname, "idade": idade, "email": email, "endereco": endereco, "senha": senha, "cpf": cpf}

    def pede_nickname(self, mensagem):
        nickname = input(mensagem)
        return nickname

    def pede_senha(self):
        senha = input("Insira sua senha: ")
        return senha

    def valor_deposito(self):
        valor = float(input("Insira a quantia que deseja depositar: "))
        return valor

    def dados_alteracao(self):
        print("----- ALTERAR DADOS DO USUÁRIO -----")
        nome = input("Novo Nome (deixe em branco para manter o atual): ")
        nickname = input("Novo Nickname (deixe em branco para manter o atual): ")
        idade = input("Nova Idade (deixe em branco para manter a atual): ")
        email = input("Novo E-mail (deixe em branco para manter o atual): ")
        endereco = input("Novo Endereço (deixe em branco para manter o atual): ")
        senha = input("Nova Senha (deixe em branco para manter a atual): ")

        return {
            "nome": nome if nome else None,
            "nickname": nickname if nickname else None,
            "idade": int(idade) if idade else None,
            "email": email if email else None,
            "endereco": endereco if endereco else None,
            "senha": senha if senha else None
        }

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")

    def alterar_usuario():
        pass
