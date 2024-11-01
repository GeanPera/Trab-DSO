from limite.tela_sistema import TelaSistema
from controle.controlador_jogos import ControladorJogos
from controle.controlador_usuarios import ControladorUsuarios
from controle.controlador_compra import ControladorCompra


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__controlador_jogos = ControladorJogos(self)
        self.__controlador_compra = ControladorCompra(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    @property
    def controlador_jogos(self):
        return self.__controlador_jogos

    @property
    def controlador_compra(self):
        return self.__controlador_compra

    def inicializa_sistema(self):
        self.__tela_sistema.mostra_mensagem("Bem-vindo!")
        self.inicializa_jogos()
        self.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mensagem("Sistema encerrado com sucesso.")
        exit(0)

    def inicializa_jogos(self):
        self.__controlador_jogos.novo_jogo("The Legend of Zelda", "Aventura", "Nintendo", 12, "Aventura épica", 59.99, 1000)
        self.__controlador_jogos.novo_jogo("Super Mario", "Plataforma", "Nintendo", 7, "Jogo clássico", 39.99, 1500)
        self.__controlador_jogos.novo_jogo("Final Fantasy", "RPG", "Square Enix", 16, "RPG envolvente", 69.99, 500)
        self.__controlador_jogos.novo_jogo("The Witcher 3", "RPG", "CD Projekt Red", 18, "Mundo aberto e denso", 89.99, 2000)
        self.__controlador_jogos.novo_jogo("Cyberpunk 2077", "Ação", "CD Projekt Red", 18, "Futurístico", 199.99, 2000)
        self.__controlador_jogos.novo_jogo("FIFA 22", "Esportes", "EA Sports", 3, "Simulador de futebol", 49.99, 3000)
        self.__controlador_jogos.novo_jogo("NBA 2K22", "Esportes", "2K Games", 3, "Simulador de basquete", 59.99, 2500)
        self.__controlador_jogos.novo_jogo("Among Us", "Casual", "InnerSloth", 10, "Jogo de dedução social", 9.99, 4000)

    def usuario_tela(self):
        self.__controlador_usuarios.abre_tela()

    def loja_tela(self):
        self.__controlador_jogos.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.loja_tela, 2: self.usuario_tela, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except KeyError:
                self.__tela_sistema.mostra_mensagem("Opção inválida. Tente novamente.")
