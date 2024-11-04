from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario

class ControladorUsuarios():
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    @property
    def usuarios(self):
        return self.__usuarios
    
    def encontrar_usuario(self, nickname):
        for usuario in self.__usuarios:
            if usuario.nickname == nickname:
                return usuario
        return False


    def cadastrar(self):
        dados_usuario = self.__tela_usuario.dados_usuario()
        for usuario in self.__usuarios:
            if self.encontrar_usuario(dados_usuario["cpf"]):
                mensagem = "CPF já utilizado!"
                self.__tela_usuario.mostra_mensagem()
                return

            elif usuario.email == dados_usuario["email"]: 
                mensagem = "E-mail já utilizado!"
                self.__tela_usuario.mostra_mensagem()
                return

            elif usuario.nickname == dados_usuario["nickname"]:
                mensagem = "Nickname já utilizado!"
                self.__tela_usuario.mostra_mensagem()
                return

        novo_usuario = Usuario(dados_usuario["nome"], dados_usuario["nickname"], dados_usuario["idade"], dados_usuario["email"], dados_usuario["endereco"], dados_usuario["senha"], dados_usuario["cpf"], 0)
        self.__usuarios.append(novo_usuario)
        self.__tela_usuario.mostra_mensagem("O usuário foi cadastrado com sucesso!")

    def alterar_usuario(self):
        
        while True:
            mensagem = "Insira o nickname do usuário a ser alterado: "
            nickname = self.__tela_usuario.pede_nickname(mensagem)
            if nickname == 0:
                self.abre_tela()
            if self.encontrar_usuario(nickname):
                usuario_encontrado = self.encontrar_usuario(nickname)
                senha = self.__tela_usuario.pede_senha()
                if senha == usuario_encontrado.senha:
                
                    novos_dados = self.__tela_usuario.dados_alteracao()
                    usuario_encontrado.nome = novos_dados.get("nome", usuario_encontrado.nome)
                    usuario_encontrado.nickname = novos_dados.get("nickname", usuario_encontrado.nickname)
                    usuario_encontrado.idade = novos_dados.get("idade", usuario_encontrado.idade)
                    usuario_encontrado.email = novos_dados.get("email", usuario_encontrado.email)
                    usuario_encontrado.endereco = novos_dados.get("endereco", usuario_encontrado.endereco)
                    usuario_encontrado.senha = novos_dados.get("senha", usuario_encontrado.senha)
                    self.__tela_usuario.mostra_mensagem("Dados do usuário alterados com sucesso!")
                    return
                else:
                    self.__tela_usuario.mostra_mensagem("Senha incorreta!")

            else:
                self.__tela_usuario.mostra_mensagem("Usuário não encontrado, tente novamente ou digite 0 para voltar pro menu anterior.")

    def adicionar_amigo(self):
            while True:
                mensagem = "Insira seu nickname: "
                nick_usuario = self.__tela_usuario.pede_nickname(mensagem)

                if nick_usuario == "0":
                    self.abre_tela()
                if not self.encontrar_usuario(nick_usuario):
                    self.__tela_usuario.mostra_mensagem("Usuário não encontrado, tente novamente ou digite 0 para voltar pro menu anterior.")
                else:
                    usuario = self.encontrar_usuario(nick_usuario)
                    break

            while True:
                mensagem = "Insira o nickname do usuário que você deseja adicionar: "
                nick_amigo = self.__tela_usuario.pede_nickname(mensagem)

                if nick_amigo == "0":
                    self.abre_tela()

                if not self.encontrar_usuario(nick_amigo):
                    self.__tela_usuario.mostra_mensagem("Usuário não encontrado, tente novamente ou digite 0 para voltar pro menu anterior.")
                else:
                    amigo = self.encontrar_usuario(nick_amigo)
                    break

            if amigo in usuario.amigos:
                self.__tela_usuario.mostra_mensagem("Esse usuário já está na sua lista de amigos!")
                return

            if (usuario.idade >= 18 <= amigo.idade) or (usuario.idade < 18 and amigo.idade < 18):
                usuario.amigos.append(amigo)
                amigo.amigos.append(usuario)
                self.__tela_usuario.mostra_mensagem(f"{amigo.nickname} foi adicionado à sua lista de amigos!")
                return
            else:
                self.__tela_usuario.mostra_mensagem("Não foi possível adicionar esse usuário! As faixas etárias não são compatíveis.")
                return

    def mostrar_amigos(self):
        nick_usuario = self.__tela_usuario.pede_nickname("Insira seu nickname: ")
        usuario = self.encontrar_usuario(nick_usuario)
        self.__tela_usuario.mostra_mensagem("seus Amigos:")
        for amigo in usuario.amigos:
            self.__tela_usuario.mostra_mensagem(f"- {amigo.nome}")

    def excluir_amigo(self):
        while True:
            mensagem = "Insira seu nickname: "
            nick_usuario = self.__tela_usuario.pede_nickname(mensagem)

            if nick_usuario == "0":
                self.abre_tela()

            if not self.encontrar_usuario(nick_usuario):
                self.__tela_usuario.mostra_mensagem("Usuário não encontrado, tente novamente ou digite 0 para voltar pro menu anterior.")

            else:
                usuario = self.encontrar_usuario(nick_usuario)
                break

        while True:
            mensagem = "Insira o nickname do usuário que você deseja excluir: "
            nick_amigo = self.__tela_usuario.pede_nickname(mensagem)

            if nick_amigo == "0":
                self.abre_tela()

            if not self.encontrar_usuario(nick_amigo):
                self.__tela_usuario.mostra_mensagem("Usuário não encontrado, tente novamente ou digite 0 para voltar pro menu anterior.")

            else:
                amigo = self.encontrar_usuario(nick_amigo)
                break

        if amigo not in usuario.amigos:
            self.__tela_usuario.mostra_mensagem("Esse usuário não está na sua lista de amigos!")
            return

        usuario.amigos.remove(amigo)
        amigo.amigos.remove(usuario)
        self.__tela_usuario.mostra_mensagem(f"{amigo.nickname} foi removido da sua lista de amigos!")

    def depositar_saldo(self):
        while True:
            mensagem = "Insira seu nickname: "
            nick_usuario = self.__tela_usuario.pede_nickname(mensagem)
            senha = self.__tela_usuario.pede_senha()
            usuario = self.encontrar_usuario(nick_usuario)
            
            if nick_usuario == "0":
                self.abre_tela()
                
            if not senha == usuario.senha:
                self.__tela_usuario.mostra_mensagem("Senha inválida! Tente novamente ou digite 0 para voltar pro menu anterior.")
            
            if not self.encontrar_usuario(nick_usuario):
                self.__tela_usuario.mostra_mensagem("Usuário não encontrado, tente novamente ou digite 0 para voltar pro menu anterior.")
            
            else:
                usuario = self.encontrar_usuario(nick_usuario)
                break
        
        valor = self.__tela_usuario.valor_deposito()
        usuario.saldo += valor
        self.__tela_usuario.mostra_mensagem(f"Depósito realizado! Seu saldo atual é R${usuario.saldo:.2f}")
    
    def verificar_saldo(self):
        while True:
            mensagem = "Insira seu nickname: "
            nick_usuario = self.__tela_usuario.pede_nickname(mensagem)
            senha = self.__tela_usuario.pede_senha()
            usuario = self.encontrar_usuario(nick_usuario)
            
            if nick_usuario == "0":
                self.abre_tela()
                
            if not senha == usuario.senha:
                self.__tela_usuario.mostra_mensagem("Senha inválida! Tente novamente ou digite 0 para voltar pro menu anterior.")
            
            if not self.encontrar_usuario(nick_usuario):
                self.__tela_usuario.mostra_mensagem("Usuário não encontrado, tente novamente ou digite 0 para voltar pro menu anterior.")
            
            else:
                usuario = self.encontrar_usuario(nick_usuario)
                self.__tela_usuario.mostra_mensagem(f"Seu saldo é R${usuario.saldo:.2f}")
                return

    def adicionar_jogo(self, jogo, usuario):
        for game in usuario.jogos:
            if game == jogo:
                return "Você já possui esse jogo!"
        usuario.jogos.append(jogo)
        usuario.saldo -= jogo.preco
        return f"Jogo comprado com sucesso! Seu saldo atual é R${usuario.saldo}"

    def presentear_amigo(self, jogo, amigo, usuario):
        for game in amigo.jogos:
            if game == jogo:
                return "Você já possui esse jogo!"
        amigo.jogos.append(jogo)
        usuario.saldo -= jogo.preco
        return f"Jogo enviado com sucesso! Seu saldo atual é R${usuario.saldo}"

    def relatorio_usuarios(self):
        relatorios = []
        for usuario in self.__usuarios:
            total_gasto = sum(jogo.preco for jogo in usuario.jogos)
            amigos = [amigo.nickname for amigo in usuario.amigos]
            relatorios.append(f"Nome: {usuario.nome}, Nickname: {usuario.nickname}, Idade: {usuario.idade}, Saldo: {usuario.saldo}, Quantidade de Jogos Comprados: {len(usuario.jogos)}, Total Gasto: {total_gasto}, Amigos: {', '.join(amigos) if amigos else 'Sem amigos'}")
        return relatorios
    def meus_jogos(self):
        nickname = self.__tela_usuario.pede_nickname("Qual seu Nickname?")
        usuario = self.encontrar_usuario(nickname)
        self.__tela_usuario.mostra_mensagem("Seus jogos:")
        for jogo in usuario.jogos:
            self.__tela_usuario.mostra_mensagem(f"- {jogo.titulo}")
    def retornar(self):
        self.__tela_usuario.mostra_mensagem("Retornando ao menu principal...")
        return

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar, 2: self.alterar_usuario, 3: self.adicionar_amigo, 4: self.excluir_amigo, 5: self.depositar_saldo, 6: self.meus_jogos, 7: self.mostrar_amigos, 8: self.verificar_saldo, 0: self.retornar}

        continua = True
        while continua:
            opcao = self.__tela_usuario.opcoes_tela()
            lista_opcoes[opcao]()
            if opcao == 0:
                break
