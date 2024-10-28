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
    
    def encontrar_usuario(self, cpf):
        for usuario in self.__usuarios:
            if usuario.cpf == cpf:
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
                mensagem = "CPF já utilizado!"
                self.__tela_usuario.mostra_mensagem()
                return

            elif usuario.nickname == dados_usuario["nickname"]:
                mensagem = "CPF já utilizado!"
                self.__tela_usuario.mostra_mensagem()
                return

        novo_usuario = Usuario(dados_usuario["nome"], dados_usuario["nickname"], dados_usuario["idade"], dados_usuario["email"], dados_usuario["endereco"], dados_usuario["senha"], dados_usuario["cpf"], 0)
        self.__usuarios.append(novo_usuario)
    
    def alterar_usuario(self):
        cpf = self.__tela_usuario.pede_cpf()
        
        if self.encontrar_usuario(cpf):
            usuario_encontrado = self.encontrar_usuario(cpf)
            novos_dados = self.__tela_usuario.dados_alteracao()
            
            usuario_encontrado.nome = novos_dados.get("nome", usuario_encontrado.nome)
            usuario_encontrado.nickname = novos_dados.get("nickname", usuario_encontrado.nickname)
            usuario_encontrado.idade = novos_dados.get("idade", usuario_encontrado.idade)
            usuario_encontrado.email = novos_dados.get("email", usuario_encontrado.email)
            usuario_encontrado.endereco = novos_dados.get("endereco", usuario_encontrado.endereco)
            usuario_encontrado.senha = novos_dados.get("senha", usuario_encontrado.senha)
    
            self.__tela_usuario.mostra_mensagem("Dados do usuário alterados com sucesso!")

        else:
            self.__tela_usuario.mostra_mensagem("Usuário não encontrado.")
            
    def adicionar_amigo(self):
        cpf_user = self.__tela_usuario.pede_cpf()
        
        if not self.encontrar_usuario(cpf_user):
            self.__tela_usuario.mostra_mensagem("Usuário não encontrado.")
            return
        
        usuario = self.encontrar_usuario(cpf_user)
        
        cpf_amigo = self.__tela_usuario.pede_cpf()
        
        if not self.encontrar_usuario(cpf_amigo):
            self.__tela_usuario.mostra_mensagem("Usuário não encontrado.")
            return
        
        amigo = self.encontrar_usuario(cpf_amigo)
        
        if amigo in usuario.amigos:
            self.__tela_usuario.mostra_mensagem("Esse usuário já está na sua lista de amigos!")
            return
        
        usuario.amigos.append(amigo)
        amigo.amigos.append(usuario)
        self.__tela_usuario.mostra_mensagem(f"{amigo.nome} foi adicionado à sua lista de amigos!")

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar, 2: self.alterar_usuario, 3: self.adicionar_amigo}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.opcoes_tela()]()