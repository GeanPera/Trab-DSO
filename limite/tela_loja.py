import PySimpleGUI as sg


class TelaLoja:

    def __init__(self):
        self.__window = None
        self.init_components()

    def exibir_menu(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def solicitar_genero(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- Gênero ----------', font=("Helvica", 25))],
            [sg.Text('Digite o Gênero:', size=(15, 1)), sg.InputText('', key='gen')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        genero = values['gen']

        self.close()
        return genero

    def solicitar_desenvolvedora(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- Desenvolvedora ----------', font=("Helvica", 25))],
            [sg.Text('Nome da Desenvolvedora:', size=(15, 1)), sg.InputText('', key='dev')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        desenvolvedora = values['dev']

        self.close()
        return desenvolvedora

    def solicitar_faixa_preco(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- Faixa de Preço ----------', font=("Helvica", 25))],
            [sg.Text('Min:', size=(15, 1)), sg.InputText('', key='min')],
            [sg.Text('Max:', size=(15, 1)), sg.InputText('', key='max')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        minimo = values['min']
        maximo = values['max']

        self.close()
        return minimo, maximo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Menu da Loja', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Todos os Jogos',"RD1", key='1')],
            [sg.Radio('Jogo mais Comprado',"RD1", key='2')],
            [sg.Radio('Jogos por gênero',"RD1", key='3')],
            [sg.Radio('Jogos por desenvolvedora',"RD1", key='4')],
            [sg.Radio('Filtrar por preço',"RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('Sistema de jogos').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values