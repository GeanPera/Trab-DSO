from limite.tela_usuario import TelaUsuario
from entidade.usuario import Usuario
from exceptions.campo_vazio_exception import CamposVaziosError
from exceptions.amigo_repetido_exception import AmigoRepetidoError
from exceptions.usuario_nao_encontrado_exception import UsuarioNaoEncontradoError
from exceptions.campo_ja_utilizado_exception import DadoJaUtilizadoError
import pickle
from DAOs.usuario_dao import UsuarioDAO

class ControladorUsuarios():
    def __init__(self, controlador_sistema):
        self.__usuarios_dao = UsuarioDAO()
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema


    @property
    def usuarios(self):
        return self.__usuarios
    
    def encontrar_usuario(self, nickname):
        for usuario in self.__usuarios_dao.get_all():
            if usuario.nickname == nickname:
                return usuario
        return None


    def cadastrar(self):
        while True:
            try:
                dados_usuario = self.__tela_usuario.dados_usuario()
                
                if dados_usuario == 0:
                    return

                if not all(dados_usuario.values()):
                    raise CamposVaziosError
                
                for usuario in self.__usuarios_dao.get_all():
                    if self.encontrar_usuario(dados_usuario["cpf"]):
                        mensagem = "CPF já utilizado!"
                        raise DadoJaUtilizadoError(mensagem)

                    elif usuario.email == dados_usuario["email"]: 
                        mensagem = "E-mail já utilizado!"
                        raise DadoJaUtilizadoError(mensagem)

                    elif usuario.nickname == dados_usuario["nickname"]:
                        mensagem = "Nickname já utilizado!"
                        raise DadoJaUtilizadoError(mensagem)

                if len(dados_usuario["nickname"]) < 4:
                    mensagem = "Seu nickname precisa ter pelo menos 4 caracteres"
                    self.__tela_usuario.mostra_mensagem(mensagem)
                    return

                novo_usuario = Usuario(dados_usuario["nome"], dados_usuario["nickname"], dados_usuario["idade"], dados_usuario["email"], dados_usuario["endereco"], dados_usuario["senha"], dados_usuario["cpf"], 0)
                self.__usuarios_dao.add(novo_usuario)
                self.__tela_usuario.mostra_mensagem("O usuário foi cadastrado com sucesso!")
                return
            
            except CamposVaziosError as mensagem:
                self.__tela_usuario.mostra_mensagem(str(mensagem))
                
            except DadoJaUtilizadoError as mensagem:
                self.__tela_usuario.mostra_mensagem(str(mensagem))

    def alterar_usuario(self):
        while True:
            try:
                self.__tela_usuario.mostra_mensagem("Insira seu nickname")
                nickname = self.__tela_usuario.pede_nickname()
                
                if nickname == 0:
                    return

                if not self.encontrar_usuario(nickname):
                    raise UsuarioNaoEncontradoError
                    
                usuario_encontrado = self.encontrar_usuario(nickname)
                senha = self.__tela_usuario.pede_senha()
                if senha == usuario_encontrado.senha:
                
                    novos_dados = self.__tela_usuario.alterar_dados()
                    for usuario in self.__usuarios:

                        if usuario.email == novos_dados["email"]: 
                            mensagem = "E-mail já utilizado!"
                            self.__tela_usuario.mostra_mensagem(mensagem)
                            return

                        elif usuario.nickname == novos_dados["nickname"]:
                            mensagem = "Nickname já utilizado!"
                            self.__tela_usuario.mostra_mensagem(mensagem)
                            return
                    
                    if len(usuario_encontrado.nickname) < 4:
                        self.__tela_usuario.mostra_mensagem("Seu nickname precisa ter pelo menos 4 caracteres")
                    else:
                        usuario_encontrado.nome = novos_dados.get("nome", usuario_encontrado.nome)
                        usuario_encontrado.nickname = novos_dados.get("nickname", usuario_encontrado.nickname)
                        usuario_encontrado.idade = novos_dados.get("idade", usuario_encontrado.idade)
                        usuario_encontrado.email = novos_dados.get("email", usuario_encontrado.email)
                        usuario_encontrado.endereco = novos_dados.get("endereco", usuario_encontrado.endereco)
                        usuario_encontrado.senha = novos_dados.get("senha", usuario_encontrado.senha)
                        self.__usuarios_dao.update(usuario_encontrado)
                        self.__tela_usuario.mostra_mensagem("Dados do usuário alterados com sucesso!")
                        return
                else:
                    self.__tela_usuario.mostra_mensagem("Senha incorreta!")

            except UsuarioNaoEncontradoError as e:
                self.__tela_usuario.mostra_mensagem(str(e))

            
    def excluir_usuario(self):
        while True:
            try:
                nick_usuario = self.__tela_usuario.pede_nickname()
                
                if nick_usuario == 0:
                    return

                if not self.encontrar_usuario(nick_usuario):
                    raise UsuarioNaoEncontradoError

                else:
                    usuario = self.encontrar_usuario(nick_usuario)
                    
                self.__tela_usuario.mostra_mensagem("Você está excluindo seu usuário. Ao confirmar, você nao poderá reverter esse processo. Para confirmar, digite sua senha abaixo.")
                senha = self.__tela_usuario.pede_senha()
                if usuario.senha == senha:
                    self.__tela_usuario.mostra_mensagem(f"O usuário {usuario.nickname} foi excluído com sucesso!")
                    self.__usuarios_dao.remove(usuario)
                else:
                    self.__tela_usuario.mostra_mensagem("Senha Incorreta!")
                
            except UsuarioNaoEncontradoError as e:
                self.__tela_usuario.mostra_mensagem(str(e))
            
    def adicionar_amigo(self):
            while True:
                try:
                    self.__tela_usuario.mostra_mensagem("Insira seu nickname")
                    nick_usuario = self.__tela_usuario.pede_nickname()
                    
                    if nick_usuario == 0:
                        return

                    if not self.encontrar_usuario(nick_usuario):
                        raise UsuarioNaoEncontradoError
                    else:
                        usuario = self.encontrar_usuario(nick_usuario)
                        

                    self.__tela_usuario.mostra_mensagem("Insira o nickname do usuário que você deseja adicionar: ") 
                    nick_amigo = self.__tela_usuario.pede_nickname()
                    
                    if nick_amigo == 0:
                        return

                    if not self.encontrar_usuario(nick_amigo):
                        raise UsuarioNaoEncontradoError
                    else:
                        amigo = self.encontrar_usuario(nick_amigo)
                        
                    if usuario == amigo:
                        raise AmigoRepetidoError(nick_amigo)
                    
                    if amigo in usuario.amigos:
                        raise AmigoRepetidoError(nick_amigo)

                    if (usuario.idade >= 18 <= amigo.idade) or (usuario.idade < 18 and amigo.idade < 18):
                        usuario.amigos.append(amigo)
                        amigo.amigos.append(usuario)
                        self.__tela_usuario.mostra_mensagem(f"{amigo.nickname} foi adicionado à sua lista de amigos!")
                        return
                    else:
                        self.__tela_usuario.mostra_mensagem("Não foi possível adicionar esse usuário! As faixas etárias não são compatíveis.")
                        return
                except AmigoRepetidoError as e:
                    self.__tela_usuario.mostra_mensagem(str(e))
                    
                except UsuarioNaoEncontradoError as e:
                    self.__tela_usuario.mostra_mensagem(str(e))


    def mostrar_amigos(self):
        nick_usuario = self.__tela_usuario.pede_nickname()
        
        if nick_usuario == 0:
            return
        
        usuario = self.encontrar_usuario(nick_usuario)
        if len(usuario.amigos) == 0:
            self.__tela_usuario.mostra_mensagem('Você ainda nao possui amigos!')
            return
        self.__tela_usuario.mostra_mensagem("seus Amigos:")
        for amigo in usuario.amigos:
            self.__tela_usuario.mostra_mensagem(f"- {amigo.nome}")

    def excluir_amigo(self):
        while True:
            try:
                self.__tela_usuario.mostra_mensagem("Insira seu nickname")
                nick_usuario = self.__tela_usuario.pede_nickname()

                if nick_usuario == 0:
                    return

                if not self.encontrar_usuario(nick_usuario):
                    raise UsuarioNaoEncontradoError

                else:
                    usuario = self.encontrar_usuario(nick_usuario)

                self.__tela_usuario.mostra_mensagem("Insira o nickname do usuário que você deseja excluir:")
                nick_amigo = self.__tela_usuario.pede_nickname()
                
                if nick_amigo == 0:
                    return

                if not self.encontrar_usuario(nick_amigo):
                    raise UsuarioNaoEncontradoError

                else:
                    amigo = self.encontrar_usuario(nick_amigo)
                    

                if amigo not in usuario.amigos:
                    self.__tela_usuario.mostra_mensagem("Esse usuário não está na sua lista de amigos!")
                    return

                usuario.amigos.remove(amigo)
                amigo.amigos.remove(usuario)
                self.__tela_usuario.mostra_mensagem(f"{amigo.nickname} foi removido da sua lista de amigos!")
                return
            except UsuarioNaoEncontradoError as e:
                self.__tela_usuario.mostra_mensagem(str(e))


    def depositar_saldo(self):
        try:
            while True:
                mensagem = "Insira seu nickname: "
                nick_usuario = self.__tela_usuario.pede_nickname()
                senha = self.__tela_usuario.pede_senha()
                usuario = self.encontrar_usuario(nick_usuario)
                
                if nick_usuario == 0 or senha == 0:
                    return
                    
                if not senha == usuario.senha:
                    self.__tela_usuario.mostra_mensagem("Senha inválida! Tente novamente ou digite 0 para voltar pro menu anterior.")
                
                if not self.encontrar_usuario(nick_usuario):
                    raise UsuarioNaoEncontradoError
                
                else:
                    usuario = self.encontrar_usuario(nick_usuario)
                    break
            
            valor = self.__tela_usuario.valor_deposito()
            
            if valor == 0:
                return
            
            usuario.saldo += valor
            self.__usuarios_dao.update(usuario)
            self.__tela_usuario.mostra_mensagem(f"Depósito realizado! Seu saldo atual: R${usuario.saldo:.2f}")
        except UsuarioNaoEncontradoError as e:
            self.__tela_usuario.mostra_mensagem(str(e))

    
    def verificar_saldo(self):
        try:
            while True:
                nick_usuario = self.__tela_usuario.pede_nickname()
                senha = self.__tela_usuario.pede_senha()
                
                if nick_usuario == 0 or senha == 0:
                    return
                usuario = self.encontrar_usuario(nick_usuario)
                    
                if not senha == usuario.senha:
                    self.__tela_usuario.mostra_mensagem("Senha inválida! Tente novamente ou digite 0 para voltar pro menu anterior.")
                
                if not self.encontrar_usuario(nick_usuario):
                    raise UsuarioNaoEncontradoError
                
                else:
                    usuario = self.encontrar_usuario(nick_usuario)
                    self.__tela_usuario.mostra_mensagem(f"Seu saldo: R${usuario.saldo:.2f}")
                    return
        except UsuarioNaoEncontradoError as e:
            self.__tela_usuario.mostra_mensagem(str(e))

    def adicionar_jogo(self, jogo, usuario):
        for game in usuario.jogos:
            if game.titulo == jogo.titulo:
                return None
        usuario.jogos.append(jogo)
        usuario.saldo -= jogo.preco
        self.__usuarios_dao.update(usuario)
        return "Jogo adicionado"

    def presentear_amigo(self, jogo, amigo, usuario):
        for game in amigo.jogos:
            if game == jogo:
                return "O usuário já possui esse jogo!"
        amigo.jogos.append(jogo)
        usuario.saldo -= jogo.preco
        return f"Jogo enviado com sucesso! Seu saldo atual é R${usuario.saldo}"

    def relatorio_usuarios(self):
        relatorios = []
        for usuario in self.__usuarios_dao.get_all():
            total_gasto = sum(jogo.preco for jogo in usuario.jogos)
            amigos = [amigo.nickname for amigo in usuario.amigos]
            relatorios.append(f"Nome: {usuario.nome}, Nickname: {usuario.nickname}, Idade: {usuario.idade}, Saldo: {usuario.saldo}, Quantidade de Jogos Comprados: {len(usuario.jogos)}, Total Gasto: {total_gasto}, Amigos: {', '.join(amigos) if amigos else 'Sem amigos'}")
        return relatorios
    def meus_jogos(self):
        minha_lista_jogos = []
        try:
            nickname = self.__tela_usuario.pede_nickname()
            
            if nickname == 0:
                return
            usuario = self.encontrar_usuario(nickname)
            if usuario == None:
                raise UsuarioNaoEncontradoError
            mensagem = "Seus jogos:"
            for jogo in usuario.jogos:
                minha_lista_jogos.append({'titulo': f'{jogo.titulo}', 'descricao': jogo.descricao, 'imagem': jogo.imagem})
            self.__tela_usuario.exibir_meus_jogos(mensagem, minha_lista_jogos)
        except UsuarioNaoEncontradoError as e:
            self.__tela_usuario.mostra_mensagem(str(e))
            
    def retornar(self):
        return

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar, 2: self.alterar_usuario, 3: self.excluir_usuario, 4: self.adicionar_amigo, 5: self.excluir_amigo, 
                        6: self.depositar_saldo, 7: self.meus_jogos, 8: self.mostrar_amigos, 9: self.verificar_saldo, 0: self.retornar}

        while True:
            opcao = self.__tela_usuario.opcoes_tela()
            try:
                opcao_escolhida = lista_opcoes[opcao]
                opcao_escolhida()
                if opcao == 0:
                    break
            except KeyError:
                self.__tela_usuario.mostra_mensagem("Opçao inválida")
