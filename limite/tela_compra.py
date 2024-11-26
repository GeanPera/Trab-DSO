import PySimpleGUI as sg


class TelaCompra:
    def opcao_compra(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if button == 'Comprar':
            opcao = 1
        if button == 'Presentear':
            opcao = 2
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button == 'Retornar':
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Push(), sg.Text('Opções de Compra', font=("Verdana",25), colors='Cyan'), sg.Push()],
            [sg.Push(), sg.Button('Comprar', button_color="#06598a", size= 20), sg.Push()],
            [sg.Push(), sg.Button('Presentear', button_color="#06598a", size= 20), sg.Push()],
            [sg.Push(), sg.Cancel('Retornar'), sg.Push()]
        ]
        self.__window = sg.Window('Sistema de jogos').Layout(layout)

    def pede_nickname(self, mensagem):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text(mensagem, font=("Verdana",12))],
            [sg.InputText('', key='nick')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        nickname = values['nick']

        self.close()
        return nickname
    
    def pede_senha(self):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text('Insira sua senha:', font=("Verdana",12))],
            [sg.InputText('', key='senha')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        senha = values['senha']

        self.close()
        return senha

    def solicitar_jogo(self, mensagem):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text(mensagem, font=("Verdana",12))],
            [sg.InputText('', key='jogo')],
            [sg.Button('Confirmar')]
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
