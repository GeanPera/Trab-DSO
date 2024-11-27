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
                
    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGray8')
        
        layout = [
            
            [sg.Push(), sg.Text('SIN Games', font=("Minecrafter Alt", 35), colors='LightGray', pad=10), sg.Push()],
            [sg.Push(), sg.Text('Escolha uma opçao!', font=("Minecraft", 20), pad=15, colors="#f7cb05"), sg.Push()],
            [sg.Push(), sg.Button('Loja', key='-Loja-', button_color=("White", "#1c1d1f"), size= 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('⚙️ Opçoes de Usuário', key='-Opcoes-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70", tooltip='Cadastre um usuário, acesse sua lista de jogos e amigos, ou realize um depósito'), sg.Push()],
            [sg.Push(), sg.Button('📄 Relatórios', key='-Relatorios-', button_color=("White", "#1c1d1f"), size = 25, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Cancel('Encerrar sessao', button_color=("White", "Red"), pad = 25, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('SIN Games', size=(600, 500), border_depth=15).Layout(layout)

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")
        
        