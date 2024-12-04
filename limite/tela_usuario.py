import PySimpleGUI as sg
import pygame

class TelaUsuario():
    def __init__(self):
        self.__window = None
        self.init_components()
        pygame.mixer.init()

    def opcoes_tela(self):
        self.init_components()
        while True:
            button, values = self.__window.read()
            opcao = 0
            if button == '-Cadastro-':
                self.som()
                opcao = 1
            if button == '-Alterar-':
                self.som()
                opcao = 2
            if button == '-Excluir-':
                self.som()
                opcao = 3
            if button == '-Adicionar-':
                self.som()
                opcao = 4
            if button == '-Remover-':
                self.som()
                opcao = 5
            if button == '-Depositar-':
                self.som()
                opcao = 6
            if button == '-Jogos-':
                self.som()
                opcao = 7
            if button == '-Amigos-':
                self.som()
                opcao = 8
            if button == '-Saldo-':
                self.som()
                opcao = 9
            if button == '-Retornar-':
                self.som()
                opcao = 0
            self.close()
            return opcao
            

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGray8')
        
        layout = [
            [sg.Push(), sg.Text('Opçoes de usuário', font=('Minecraft', 25), pad=30, colors='#f7cb05'), sg.Push()],
            [sg.Push(), sg.Button('+ Novo Cadastro', key='-Cadastro-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('📝 Alterar Cadastro', key='-Alterar-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('❌ Excluir Usuário', key='-Excluir-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('👤 Adicionar Amigo', key='-Adicionar-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('💔 Remover Amigo', key='-Remover-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('💰 Depositar Saldo', key='-Depositar-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('🎮 Meus Jogos', key='-Jogos-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('👥 Meus Amigos', key='-Amigos-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('$ Verificar Saldo', key='-Saldo-', button_color=("White", "#1c1d1f"), size= 20, font=("Minecraft", 15), mouseover_colors="#6e6f70"), sg.Push()],
            [sg.Push(), sg.Button('↩️ Retornar', key='-Retornar-', button_color=("White", "Red"), size= 15, pad = 25, font=("Minecraft", 15)), sg.Push()]
            
            
        ]
        self.__window = sg.Window('Opções de usuário', size=(700,650)).Layout(layout)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    def ativar_som(self):
        pygame.mixer.init()
        
    def som(self):
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play()

    def dados_usuario(self):
        self.novo_cadastro()
        while True:
            event, values = self.__window.read()
            if event == '-confirmar-':
                nome = values['-nome-']
                nick = values['-nick-']
                idade = int(values['-idade-'])
                email = values['-email-']
                endereco = values['-endereco-']
                senha = values['-senha-']
                cpf = values['-cpf-']

                self.close()
                return {"nome": nome, "nickname": nick, "idade": idade, "email": email, "endereco": endereco, "senha": senha, "cpf": cpf}

            if event == '-Retornar-':
                self.close()
                return 0
            
    def novo_cadastro(self):
        sg.ChangeLookAndFeel('DarkGray8')

        layout = [
            [sg.Push(), sg.Text('Insira suas informaçoes!', font=('Minecraft', 25), pad=30, colors='White'), sg.Push()],
            [sg.Text('Nome:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-nome-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Nickname:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-nick-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Idade:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-idade-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('E-mail:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-email-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Endereço:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-endereco-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Senha:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-senha-', background_color='Gray', size=100, text_color='Black', password_char='*')],
            [sg.Text('CPF:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-cpf-', background_color='Gray', size=100, text_color='Black')],
            [sg.Push(), sg.Button('Realizar Cadastro', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15)), sg.Push(), sg.Button('Retornar', key='-Retornar-', button_color=("White", "Red"), size= 30, font=("Minecraft", 15)), sg.Push()]

        ]
        self.__window = sg.Window('Cadastro', size=(700, 500)).Layout(layout)

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
            return 0
        
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
            return 0

    def valor_deposito(self):
        sg.ChangeLookAndFeel('DarkGray8')
        layout = [
            [sg.Push(), sg.Text('Insira o valor que deseja depositar', font=('Minecraft', 20), pad=15, colors='White'), sg.Push()],
            [sg.Text('Valor:', font=('Minecraft', 15), pad=2, colors='LightGray'), sg.InputText('', key='-deposito-', background_color='Gray', size=100, text_color='Black')],
            [sg.Push(), sg.Button('Depositar', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15)), sg.Push(), sg.Button('Retornar', key='-Retornar-', button_color=("White", "Red"), size= 30, font=("Minecraft", 15)), sg.Push()]
        ]
        self.__window = sg.Window('Solicitar deposito', size=(600, 200)).Layout(layout)

        button, values = self.open()
        deposito = float(values['-deposito-'])
        self.som()
        self.close()
        if button == '-confirmar-':
            if deposito < 0:
                self.mostra_mensagem("O depósito precisa ser maior que R$00,00")
                return 0
            else:
                return deposito
        elif button == '-Retornar-':
            return 0

    def alterar_dados(self):
        sg.ChangeLookAndFeel('DarkGray8')

        layout = [
            [sg.Push(), sg.Text('Insira os novos dados!', font=('Minecraft', 25), pad=10, colors='Yellow'), sg.Push()],
            [sg.Push(), sg.Text('(Deixe em branco para manter o atual)', font=('Minecraft', 15), pad=10, colors='White'), sg.Push()],
            [sg.Text('Nome:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-nome-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Nickname:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-nick-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Idade:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-idade-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('E-mail:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-email-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Endereço:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-endereco-', background_color='Gray', size=100, text_color='Black')],
            [sg.Text('Senha:', font=('Minecraft', 15), pad=6, colors='LightGray'), sg.InputText('', key='-senha-', background_color='Gray', size=100, text_color='Black', password_char='*')],
            [sg.Push(), sg.Button('Realizar Cadastro', pad=10, key='-confirmar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15)), sg.Push(), sg.Button('Retornar', key='-Retornar-', button_color=("White", "Red"), size= 30, font=("Minecraft", 15)), sg.Push()]

        ]
        self.__window = sg.Window('Cadastro', size=(700, 500)).Layout(layout)
        
        event, values = self.__window.read()
        if event == '-confirmar-':
            nome = values['-nome-']
            nick = values['-nick-']
            idade = values['-idade-']
            email = values['-email-']
            endereco = values['-endereco-']
            senha = values['-senha-']

            self.close()
            return {"nome": nome, "nickname": nick, "idade": idade, "email": email, "endereco": endereco, "senha": senha}

        if event == '-Retornar-':
            self.close()
            return 0

    def exibir_meus_jogos(self, mensagem, jogos):
        sg.ChangeLookAndFeel('DarkGray8')
        jogos_layout = [
            [
                sg.Image(filename=jogo['imagem'], size=(170, 80), pad=(5)),  # Imagem do jogo
                sg.Column(
                    [
                        [sg.Text(f"{jogo['titulo']}", font=('Minecraft', 15), text_color='LightGray', pad=(0, 0))],
                        [sg.Text(jogo['descricao'], font=('Minecraft', 12), text_color='LightGray', pad=(0, 0))],
                    ],
                    vertical_alignment='top',
                    pad=(0, 0),
                ),
            ]
            for jogo in jogos
        ]
        jogos_count = len(jogos)
        altura_base = 175
        altura_por_jogo = 80
        altura_max = 800
        altura_dinamica = min(altura_base + jogos_count * altura_por_jogo, altura_max)

        layout = [
            [sg.Text(mensagem, font=('Minecraft', 15), pad=(6, 10), colors='LightGray')],
            [sg.Column(jogos_layout, scrollable=True, vertical_scroll_only=True, size=(700, (altura_dinamica - 150)))],
            [sg.Push(),sg.Button('Jogar', pad=10, key='-jogar-', button_color=('White', 'DarkGreen'), size=30, font=("Minecraft", 15)), sg.Cancel('Retornar', key='-Retornar-', button_color=("White", "Red"), pad = 10, font=("Minecraft", 15))]
        ]
        self.__window = sg.Window('Lista de Jogos', size=(700, altura_dinamica), border_depth=15).Layout(layout)

        button, values = self.open()
        self.som()
        self.close()
        if button == '-jogar-':
            return True
        

    def mostra_mensagem(self, msg):
        sg.popup("", msg, font=('Minecraft', 15), text_color='#1c1d1f', background_color='Gray', button_color=("White", "#1c1d1f"))
