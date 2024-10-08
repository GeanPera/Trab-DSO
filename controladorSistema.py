from controladorUsuário import ControladorUsuarios

class ControladorSistema:
    
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        
    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios
    
    def cadastra_usuario(self):
        self.__controlador_usuarios.abre_tela()