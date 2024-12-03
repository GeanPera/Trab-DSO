import PySimpleGUI as sg
import pygame

class TelaLoja:

    def __init__(self):
        self.__window = None
        self.init_components()

    def exibir_menu(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if button == '-Todos os Jogos-':
            self.som()
            opcao = 1
        if button =='-Jogo mais Comprado-':
            self.som()
            opcao = 2
        if button =='-Jogos por gênero-':
            self.som()
            opcao = 3
        if button =='-Jogos por desenvolvedora-':
            self.som()
            opcao = 4
        if button =='-Filtrar por preço-':
            self.som()
            opcao = 5
        if button == '-Retornar-':
            self.som()
            opcao = 0
        self.close()
        return opcao

    pygame.mixer.init()
    def som(self):
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play()
    def init_components(self):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text('Menu da Loja', font=("Minecrafter Alt",35), colors='LightGray', pad=10), sg.Push()],
            [sg.Push(), sg.Text('Escolha sua opção!', font=("Minecraft", 20), pad=15, colors="#f7cb05"), sg.Push()],
            [sg.Push(), sg.Button('Todos os Jogos', key='-Todos os Jogos-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Jogo mais Comprado', key='-Jogo mais Comprado-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Jogos por gênero', key='-Jogos por gênero-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Jogos por desenvolvedora', key='-Jogos por desenvolvedora-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Filtrar por preço', key='-Filtrar por preço-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Cancel('↩️ Retornar', key='-Retornar-', button_color=("White", "Red"), pad = 30, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Menu da Loja', border_depth=15).Layout(layout)

    def solicitar_genero(self, generos):
        sg.ChangeLookAndFeel('DarkGray8')
        gen_layout = [
            [sg.Radio(genero, "RD1", key=genero, font=('Minecraft', 15), pad=0, text_color='LightGray')]
            for genero in generos
        ]

        layout = [
            [sg.Text('Generos disponiveis:', font=('Minecraft', 15), pad=3, colors='LightGray')],
            [sg.Column(gen_layout, scrollable=True, vertical_scroll_only=True, size=(400, 450), pad=(0, 1))],
            [sg.Push(),sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), font=("Minecraft", 15)), 
            sg.Cancel('Retornar', key='-Retornar-', button_color=("White", "Red"), pad = 10, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Solicitar Gen', size=(400, 600), border_depth=15).Layout(layout)

        button, values = self.open()
        self.som()
        self.close()
        for value in values:
            if values[value] == True:
                genero = value
                break
            else:
                genero = None

        if button == '-Retornar-' or (button == '-Confirmar-' and genero == None):
            return None
        else:
            return genero

    def solicitar_desenvolvedora(self, desenvolvedoras):
        sg.ChangeLookAndFeel('DarkGray8')
        devs_layout = [
            [sg.Radio(desenvolvedora, "RD1", key=desenvolvedora, font=('Minecraft', 15), pad=0, text_color='LightGray')]
            for desenvolvedora in desenvolvedoras
        ]

        layout = [
            [sg.Text('Desenvolvedoras disponiveis:', font=('Minecraft', 15), pad=3, colors='LightGray')],
            [sg.Column(devs_layout, scrollable=True, vertical_scroll_only=True, size=(400, 450), pad=(0, 1))],
            [sg.Push(),sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), font=("Minecraft", 15)), 
            sg.Cancel('Retornar', key='-Retornar-', button_color=("White", "Red"), pad = 10, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Solicitar Dev', size=(400, 600), border_depth=15).Layout(layout)

        button, values = self.open()
        print(button, values)
        self.som()
        self.close()
        for value in values:
            if values[value] == True:
                desenvolvedora = value
                break
            else:
                desenvolvedora = None

        if button == '-Retornar-' or (button == '-Confirmar-' and desenvolvedora == None):
            return None
        else:
            return desenvolvedora

    def solicitar_faixa_preco(self):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text('Insira a Faixa de Preço!', font=('Minecraft', 25), pad= 15, colors='White'), sg.Push()],
            [sg.Text('Min:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-min-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Max:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-max-', background_color='Gray', size=100, text_color='Black')],
            [sg.Push(),sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15)), sg.Cancel('Retornar', key='-Retornar-', button_color=("White", "Red"), pad = 10, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Faixa de preco', size=(600, 500), border_depth=15).Layout(layout)

        button, values = self.open()
        minimo = values['-min-']
        maximo = values['-max-']

        self.som()
        self.close()
        if button == '-confirmar-':
            return minimo, maximo
        elif button == '-Retornar-':
            return None, None

    def exibir_lista_jogos(self, mensagem, jogos):
        sg.ChangeLookAndFeel('DarkGray8')
        jogos_layout = [
            [
                sg.Image(filename=jogo['imagem'], size=(170, 80), pad=(5)),  # Imagem do jogo
                sg.Column(
                    [
                        [sg.Text(f"{jogo['texto']}", font=('Minecraft', 15), text_color='LightGray', pad=(0, 0))],
                        [sg.Text(jogo['descricao'], font=('Minecraft', 12), text_color='LightGray', pad=(0, 0))],
                    ],
                    vertical_alignment='top',
                    pad=(0, 0),
                ),
                sg.Push(),
                sg.Button('Comprar', key=f'{jogo["nome"]}', button_color=('White', 'DarkGreen'), font=("Minecraft", 15),pad=(10, 10))
            ]
            for jogo in jogos
        ]
        jogos_count = len(jogos)
        altura_base = 175
        altura_por_jogo = 80
        altura_max = 600
        altura_dinamica = min(altura_base + jogos_count * altura_por_jogo, altura_max)

        layout = [
            [sg.Text(mensagem, font=('Minecraft', 15), pad=(6, 10), colors='LightGray')],
            [sg.Column(jogos_layout, scrollable=True, vertical_scroll_only=True, size=(860, (altura_dinamica - 150)))],
            [sg.Push(), sg.Cancel('Retornar', key='-Retornar-', button_color=("White", "Red"), pad = 10, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Lista de Jogos', size=(860, altura_dinamica), border_depth=15).Layout(layout)

        button, values = self.open()
        self.som()
        self.close()
        return button

    def mostra_mensagem(self, msg):
        sg.popup("", msg, font=('Minecraft', 15), text_color='#1c1d1f', background_color='Gray', button_color=("White", "#1c1d1f"))

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values