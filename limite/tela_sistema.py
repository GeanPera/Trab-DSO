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
            if button == 'Loja':
                self.som()
                opcao = 1
            if button == 'Opçoes de Usuário':
                self.som()
                opcao = 2
            if button == 'Relatórios':
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
                
    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkBrown7')
        layout = [
            
            [sg.Push(), sg.Text('SIN Games', font=("Minecrafter Alt", 25), colors='LightGray'), sg.Push()],
            [sg.Push(), sg.Text('Escolha uma opçao!', font=("Minecraft"), colors="#f7cb05"), sg.Push()],
            [sg.Push(), sg.Button('Loja', button_color=("White", "#aaabad"), size= 20, font="Minecraft", mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Opçoes de Usuário', button_color=("White", "#aaabad"), size = 20, font="Minecraft", mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('Relatórios', button_color=("White", "#aaabad"), size = 20, font="Minecraft", mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Cancel('Encerrar sessao', button_color=("White", "Red"), pad = 10, font="Minecraft"), sg.Push()]
        ]
        self.__window = sg.Window('SIN Games', size=(600, 300)).Layout(layout)

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")
        
        