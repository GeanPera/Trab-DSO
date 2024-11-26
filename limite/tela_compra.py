import PySimpleGUI as sg


class TelaCompra:
    def opcao_compra(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Opções de Compra', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Comprar',"RD1", key='1')],
            [sg.Radio('Presentear',"RD1", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Sistema de jogos').Layout(layout)

    def pede_nickname(self, mensagem):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- Qual o nickname ----------', font=("Helvica", 25))],
            [sg.Text(mensagem, size=(15, 1)), sg.InputText('', key='nick')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        nickname = values['nick']

        self.close()
        return nickname
    
    def pede_senha(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- Qual sua senha? ----------', font=("Helvica", 25))],
            [sg.Text('Insira sua senha:', size=(15, 1)), sg.InputText('', key='senha')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        senha = values['senha']

        self.close()
        return senha

    def solicitar_jogo(self, mensagem):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- Qual Jogo? ----------', font=("Helvica", 25))],
            [sg.Text(mensagem, size=(15, 1)), sg.InputText('', key='jogo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        jogo = values['jogo']

        self.close()
        return jogo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
