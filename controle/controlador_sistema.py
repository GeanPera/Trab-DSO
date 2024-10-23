from limite.tela_sistema import TelaSistema
from controle.controlador_jogos import ControladorJogos
from controle.controlador_usuarios import ControladorUsuarios


class ControladorSistema:
    
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__controlador_jogos = ControladorJogos(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        self.abre_tela()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios
    
    def cadastra_usuario(self):
        self.__controlador_usuarios.abre_tela()

    def menu_loja(self):
        self.__controlador_jogos.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.menu_loja, 2: self.cadastra_usuario}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()