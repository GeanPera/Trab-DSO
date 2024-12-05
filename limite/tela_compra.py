import PySimpleGUI as sg
import pygame


class TelaCompra:
    def opcao_compra(self, jogo):
        self.init_components(jogo)
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
        pygame.mixer.music.load('som/sound.mp3')
        pygame.mixer.music.play()
    def init_components(self, jogo):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text('Opçoes de Compra', font=('Minecraft', 25), pad=30, colors='White'), sg.Push()],
            [sg.Push(), sg.Image(filename=jogo.imagem, size=(170, 80), pad=(5)), sg.Text(jogo.titulo, font=('Minecraft', 15), text_color='LightGray'), sg.Push()], 
            [sg.Push(), sg.Text('Escolha uma opçao!', font=("Minecraft", 20), pad=15, colors="#f7cb05"), sg.Push()],
            [sg.Push(), sg.Button('Comprar', key='-Comprar-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Presentear', key='-Presentear-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('↩️ Retornar', key='-Retornar-', button_color=("White", "Red"), size= 15, pad = 25, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Sistema de jogos').Layout(layout)

    def pede_nickname(self, mensagem):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text(mensagem, font=('Minecraft', 16), pad=15, colors='White'), sg.Push()],
            [sg.Text('Nickname:', font=('Minecraft', 15), pad=2, colors='LightGray'), sg.InputText('', key='-nick-', background_color='Gray', size=100, text_color='Black')],
            [sg.Push(), sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15)), sg.Push(), sg.Button('Retornar', key='-Retornar-', button_color=("White", "Red"), size= 30, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Solicitar nick', size=(600, 200)).Layout(layout)

        button, values = self.open()
        nick = values['-nick-']
        self.som()
        self.close()
        if button == '-confirmar-':
            return nick
        elif button == '-Retornar-':
            return None

        self.__window = sg.Window('Cadastro', size=(700, 500)).Layout(layout)

    def pede_senha(self):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text('Insira sua senha!', font=('Minecraft', 25), pad=15, colors='White'), sg.Push()],
            [sg.Text('Senha:', font=('Minecraft', 15), pad=2, colors='LightGray'), sg.InputText('', key='-senha-', background_color='Gray', size=100, text_color='Black', password_char="*")],
            [sg.Push(), sg.Button('Confirmar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15)), sg.Push(), sg.Button('Retornar', key='-Retornar-', button_color=("White", "Red"), size= 30, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Solicitar senha', size=(600, 200)).Layout(layout)

        button, values = self.open()
        senha = values['-senha-']
        self.som()
        self.close()
        if button == '-confirmar-':
            return senha
        elif button == '-Retornar-':
            return None

    def mostra_mensagem(self, msg):
        sg.popup("", msg, font=('Minecraft', 15), text_color='#1c1d1f', background_color='Gray', button_color=("White", "#1c1d1f"))

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
