import PySimpleGUI as sg
import pygame

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()
        
    def tela_opcoes(self):
        self.init_components()
        while True:
            button, values = self.__window.Read()
            opcao = 0
            if button == '-Loja-':
                self.som()
                opcao = 1
            if button == '-Opcoes-':
                self.som()
                opcao = 2
            if button == '-Relatorios-':
                self.som()
                opcao = 3
            if button == sg.WIN_CLOSED or button == 'Encerrar sessão':
                self.som()
                opcao = 0
            self.close()
            return opcao

    pygame.mixer.init()
    def som(self):
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play()
            
    def close(self):
        self.__window.Close()
    def opcoes_relatorio(self):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text('Relat0rios', font=("Minecrafter Alt",35), colors='LightGray', pad=10), sg.Push()],
            [sg.Push(), sg.Text('Escolha o relatorio!', font=("Minecraft", 20), pad=15, colors="#f7cb05"), sg.Push()],
            [sg.Push(), sg.Button('Vendas', key='1', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Jogos por Faixa Etária', key='2', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Usuários', key='3', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Jogos por Gênero', key='4', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Cancel('↩️ Retornar', key='0', button_color=("White", "Red"), pad = 30, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Opcoes relatório', size=(600, 500), border_depth=15).Layout(layout)

        button, values = self.open()

        self.som()
        self.close()
        return button

    def exibir_relatorio(self, mensagem, relatorios):
        sg.ChangeLookAndFeel('DarkGray8')
        relatorio_layout = [
            [sg.Text(relatorio, font=('Minecraft', 15), colors='LightGray')]
            for relatorio in relatorios
        ]

        count = len(relatorios)
        altura_base = 300
        altura_por_relatorio = 160
        altura_max = 600
        altura_dinamica = min(altura_base + count * altura_por_relatorio, altura_max)

        layout = [
            [sg.Text(mensagem, font=('Minecraft', 15), pad=6, colors='#f7cb05')],
            [sg.Column(relatorio_layout, scrollable=True, vertical_scroll_only=True, size=(800, altura_dinamica-150))],
            [sg.Push(), sg.Cancel('Retornar', key='0', button_color=("White", "Red"), pad = 10, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Lista de Jogos', size=(800, altura_dinamica), border_depth=15).Layout(layout)

        button, values = self.open()
        self.som()
        self.close()
        return button

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGray8')
        
        layout = [
            
            [sg.Push(), sg.Text('SIN Games', font=("Minecrafter Alt", 35), colors='LightGray', pad=10), sg.Push()],
            [sg.Push(), sg.Text('Escolha uma opçao!', font=("Minecraft", 20), pad=15, colors="#f7cb05"), sg.Push()],
            [sg.Push(), sg.Button('Loja', key='-Loja-', button_color=("White", "#1c1d1f"), size= 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Opçoes de Usuário', key='-Opcoes-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70", tooltip='Cadastre um usuário, acesse sua lista de jogos e amigos, ou realize um depósito'), sg.Push()],
            [sg.Push(), sg.Button('Relatórios', key='-Relatorios-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Cancel('Encerrar sessao', button_color=("White", "Red"), pad = 25, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('SIN Games', size=(600, 500), border_depth=15).Layout(layout)

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")

    def open(self):
        button, values = self.__window.Read()
        return button, values