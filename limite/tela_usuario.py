import PySimpleGUI as sg
import pygame

class TelaUsuario():
    def __init__(self):
        self.__window = None
        self.init_components()

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
        
    pygame.mixer.init()
    def som(self):
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play()
        
    pygame.mixer.init()
    def som(self):
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play()
        
    def dados_usuario(self):
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
        button, values = self.open()
        dados_usuario = values['-nome-']
        '''while True:
            try:
                print("-----DADOS USUÁRIO-----")
                nome = input("Nome: ")
                nickname = input("Nickname: ")
                idade = int(input("Idade: "))
                email = input("E-mail: ")
                endereco = input("Endereço: ")
                senha = input("Senha: ")
                cpf = input("CPF: ")
                return {"nome": nome, "nickname": nickname, "idade": idade, "email": email, "endereco": endereco, "senha": senha, "cpf": cpf}
            except ValueError:
                self.mostra_mensagem("Informação inválida, tente novamente!")'''
    

    def pede_nickname(self, nome):
        nickname = input(nome)
        return nickname

    def pede_senha(self):
        senha = input("Insira sua senha: ")
        return senha

    def valor_deposito(self):
        valor = float(input("Insira a quantia que deseja depositar: "))
        return valor

    def dados_alteracao(self):
        print("----- ALTERAR DADOS DO USUÁRIO -----")
        nome = input("Novo Nome (deixe em branco para manter o atual): ")
        nickname = input("Novo Nickname (deixe em branco para manter o atual): ")
        idade = input("Nova Idade (deixe em branco para manter a atual): ")
        email = input("Novo E-mail (deixe em branco para manter o atual): ")
        endereco = input("Novo Endereço (deixe em branco para manter o atual): ")
        senha = input("Nova Senha (deixe em branco para manter a atual): ")

        return {
            "nome": nome if nome else None,
            "nickname": nickname if nickname else None,
            "idade": int(idade) if idade else None,
            "email": email if email else None,
            "endereco": endereco if endereco else None,
            "senha": senha if senha else None
        }

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")
