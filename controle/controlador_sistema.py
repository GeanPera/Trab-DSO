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
        self.__controlador_jogos.novo_jogo("Red Dead Redemption 2", "Ação/Aventura", "Rockstar Games", 18, "Faroeste épico em mundo aberto", 249.99, 1500, 'imagem\Red_dead_redemption2.png')
        self.__controlador_jogos.novo_jogo("Hades", "Roguelike", "Supergiant Games", 12, "Jogo de ação com mitologia grega", 49.99, 8000, 'imagem\hades.png')
        self.__controlador_jogos.novo_jogo("Stardew Valley", "Simulação", "ConcernedApe", 3, "Simulador de fazenda e vida social", 19.99, 12000, 'imagem\stardew_valley.png')
        self.__controlador_jogos.novo_jogo("Counter-Strike: Global Offensive", "FPS", "Valve", 16, "Jogo competitivo de tiro em primeira pessoa", 00.00, 1000000, 'imagem\csgo.png')
        self.__controlador_jogos.novo_jogo("Portal 2", "Quebra-cabeça", "Valve", 10, "Jogo de puzzle com narrativa cativante", 39.99, 5000, 'imagem\portal2.png')
        self.__controlador_jogos.novo_jogo("Terraria", "Aventura/Sandbox", "Re-Logic", 10, "Jogo sandbox de exploração e construção", 19.99, 9000, 'imagem\Terraria.png')
        self.__controlador_jogos.novo_jogo("Dark Souls III", "RPG/Ação", "FromSoftware", 16, "RPG de ação desafiador", 159.99, 4000, 'imagem\dark_souls_3.png')
        self.__controlador_jogos.novo_jogo("Dota 2", "MOBA", "Valve", 10, "Jogo multiplayer online de arena de batalha", 00.00, 1200000, 'imagem\dota2.png')
        self.__controlador_jogos.novo_jogo("Hollow Knight", "Metroidvania", "Team Cherry", 7, "Aventura em um mundo subterrâneo", 29.99, 7000, 'imagem\hollow_knight.png')
        self.__controlador_jogos.novo_jogo("The Elder Scrolls V: Skyrim", "RPG", "Bethesda", 16, "Mundo aberto rico em exploração", 149.99, 10000, 'imagem\skyrim.png')
        self.__controlador_jogos.novo_jogo("Left 4 Dead 2", "FPS/Coop", "Valve", 16, "Jogo cooperativo de zumbis", 19.99, 8000, 'imagem\left4dead2.png')
        self.__controlador_jogos.novo_jogo("Rust", "Sobrevivência", "Facepunch Studios", 16, "Jogo de sobrevivência em mundo aberto", 79.99, 6000, 'imagem\Rust.png')
        self.__controlador_jogos.novo_jogo("Subnautica", "Aventura/Sobrevivência", "Unknown Worlds Entertainment", 10, "Exploração submarina e sobrevivência", 49.99, 4500, 'imagem\subnautica.png')
        self.__controlador_jogos.novo_jogo("The Forest", "Sobrevivência/Terror", "Endnight Games", 16, "Sobrevivência em uma ilha aterrorizante", 49.99, 3000, 'imagem\The_forest.png')
        self.__controlador_jogos.novo_jogo("Dead Cells", "Roguelike/Metroidvania", "Motion Twin", 12, "Jogo de ação dinâmico", 59.99, 5000, 'imagem\dead_cells.png')
        self.__controlador_jogos.novo_jogo("Final Fantasy", "RPG", "Square Enix", 16, "RPG envolvente", 69.99, 500, 'imagem\Final_fantasy.png')
        self.__controlador_jogos.novo_jogo("The Witcher 3", "RPG", "CD Projekt Red", 18, "Mundo aberto e denso", 89.99, 2000, 'imagem\The_witcher.png')
        self.__controlador_jogos.novo_jogo("Cyberpunk 2077", "Ação", "CD Projekt Red", 18, "Futurístico", 199.99, 2000, 'imagem\cyberpunk.png')
        self.__controlador_jogos.novo_jogo("FIFA 22", "Esportes", "EA Sports", 3, "Simulador de futebol", 49.99, 3000, 'imagem\Fifa22.png')
        self.__controlador_jogos.novo_jogo("NBA 2K25", "Esportes", "2K Games", 3, "Simulador de basquete", 59.99, 2500, 'imagem\imagem_nba.png')
        self.__controlador_jogos.novo_jogo("Among Us", "Casual", "InnerSloth", 10, "Jogo de dedução social", 9.99, 4000, 'imagem\Among_us.png')

    def usuario_tela(self):
        self.__controlador_usuarios.abre_tela()

    def loja_tela(self):
        self.__controlador_jogos.abre_tela()

    def relatorio(self):
        lista_opcoes = {1: self.relatorio_vendas, 2: self.relatorio_faixa_etaria,3: self.relatorio_usuarios, 4: self.relatorio_genero}
        
        while True:
            opcao_escolhida = int(self.__tela_sistema.opcoes_relatorio())
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def relatorio_vendas(self):
        mensagem = 'Relatória de Vendas:'
        relatorio_venda = self.controlador_jogos.relatorio_vendas_por_jogo()
        self.__tela_sistemas.exibir_relatorio(mensagem, relatorio_venda)

    def relatorio_faixa_etaria():
        relatorio_faixa_etaria = self.controlador_jogos.relatorio_jogos_por_faixa_etaria()

    def relatorio_usuarios():
        relatorio_usuarios = self.controlador_usuarios.relatorio_usuarios()

    def relatorio_genero():
        relatorio_genero = self.controlador_jogos.relatorio_generos_populares()

    def abre_tela(self):
        lista_opcoes = {1: self.loja_tela, 2: self.usuario_tela,3: self.relatorio, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except KeyError:
                self.__tela_sistema.mostra_mensagem("Opção inválida. Tente novamente.")
