import PySimpleGUI as sg
import pygame


class TelaCompra:
    def opcao_compra(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if button == '-Comprar-':
            self.som()
            opcao = 1
        if button == '-Presentear-':
            self.som()
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
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
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text('Opçoes de Compra', font=('Minecraft', 25), pad=30, colors='White'), sg.Push()],
            [sg.Push(), sg.Text('Escolha uma opçao!', font=("Minecraft", 20), pad=15, colors="#f7cb05"), sg.Push()],
            [sg.Push(), sg.Button('Comprar', key='-Comprar-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Presentear', key='-Presentear-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('↩️ Retornar', key='-Retornar-', button_color=("White", "Red"), size= 15, pad = 25, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Sistema de jogos').Layout(layout)

    def pede_nickname(self, mensagem):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Text(mensagem, font=('Minecraft', 15), pad=6, colors='LightGray')],
            [sg.InputText('', key='-nick-', background_color='Gray', size=100, text_color='Black')],
            [sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        nickname = values['-nick-']

        self.som()
        self.close()
        return nickname
    
    def pede_senha(self):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Text('Insira sua senha:', font=('Minecraft', 15), pad=6, colors='LightGray')],
            [sg.InputText('', key='-senha-', background_color='Gray', size=100, text_color='Black')],
            [sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        senha = values['-senha-']

        self.som()
        self.close()
        return senha

    def solicitar_jogo(self, mensagem):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Text(mensagem, font=('Minecraft', 15), pad=6, colors='LightGray')],
            [sg.InputText('', key='jogo', background_color='Gray', size=100, text_color='Black')],
            [sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        jogo = values['jogo']

        self.som()
        self.close()
        return jogo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
