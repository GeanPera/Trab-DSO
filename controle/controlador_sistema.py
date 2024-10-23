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
        self.__controlador_jogos.novo_jogo("The Legend of Zelda", "Aventura", "Nintendo", 12, "Aventura épica", 59.99, 1000)
        self.__controlador_jogos.novo_jogo("Super Mario", "Plataforma", "Nintendo", 7, "Jogo clássico", 39.99, 1500)
        self.__controlador_jogos.novo_jogo("Final Fantasy", "RPG", "Square Enix", 16, "RPG envolvente", 69.99, 500)
        self.__controlador_jogos.novo_jogo("The Witcher 3", "RPG", "CD Projekt Red", 18, "Mundo aberto e denso", 89.99, 2000)
        self.__controlador_jogos.novo_jogo("Cyberpunk 2077", "Ação", "CD Projekt Red", 18, "Futurístico", 199.99, 2000)
        self.__controlador_jogos.novo_jogo("FIFA 22", "Esportes", "EA Sports", 3, "Simulador de futebol", 49.99, 3000)
        self.__controlador_jogos.novo_jogo("NBA 2K22", "Esportes", "2K Games", 3, "Simulador de basquete", 59.99, 2500)
        self.__controlador_jogos.novo_jogo("Among Us", "Casual", "InnerSloth", 10, "Jogo de dedução social", 9.99, 4000)
# Executa o menu interativo
        self.__controlador_jogos.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.menu_loja, 2: self.cadastra_usuario}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()