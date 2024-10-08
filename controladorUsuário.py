from telaUsuario import TelaUsuario
from usuario import Usuario

class ControladorUsuarios():
    def __init__(self):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        #self.__controlador_sistema = controlador_sistema
        
    @property
    def usuarios(self):
        return self.__usuarios
    
    def cadastrar(self):
        dados_usuario = self.__tela_usuario.dados_cadastro()
        for usuario in self.__usuarios:
            if usuario.cpf == dados_usuario.cpf:
                return "CPF já utilizado"
            
            elif usuario.email == dados_usuario.email: 
                return "E-mail já utilizado!"
            
            elif usuario.nickname == dados_usuario.nickname:
                return "Nickname já existente!"
            
        novo_usuario: Usuario(dados_usuario["nome"], dados_usuario["nickname"], dados_usuario["idade"], dados_usuario["email"], dados_usuario["endereco"], dados_usuario["senha"], dados_usuario["cpf"], 0)
        self.__usuarios.append(novo_usuario)