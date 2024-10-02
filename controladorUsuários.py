from pessoa import Pessoa
from usuario import Usuario

def ControladorUsuarios(Usuario):
    def __init__(self):
        self.__usuarios = []
        
    @property
    def usuarios(self) -> list:
        return self.__usuarios
    
    def incluir_usuario()