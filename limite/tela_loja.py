import PySimpleGUI as sg


class TelaLoja:

    def __init__(self):
        self.__window = None
        self.init_components()

    def exibir_menu(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if button == 'Todos os Jogos':
            opcao = 1
            print(opcao)
        if button =='Jogo mais Comprado':
            opcao = 2
        if button =='Jogos por gênero':
            opcao = 3
        if button =='Jogos por desenvolvedora':
            opcao = 4
        if button =='Filtrar por preço':
            opcao = 5
        if button == 'Retornar':
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Push(), sg.Text('Menu da Loja', font=("Verdana",25), colors='Cyan'), sg.Push()],
            [sg.Text('Escolha sua opção!', font=("Verdana",18))],
            [sg.Push(), sg.Button('Todos os Jogos', button_color="#06598a", size= 20), sg.Push()],
            [sg.Push(), sg.Button('Jogo mais Comprado', button_color="#06598a", size= 20), sg.Push()],
            [sg.Push(), sg.Button('Jogos por gênero', button_color="#06598a", size= 20), sg.Push()],
            [sg.Push(), sg.Button('Jogos por desenvolvedora', button_color="#06598a", size= 20), sg.Push()],
            [sg.Push(), sg.Button('Filtrar por preço', button_color="#06598a", size= 20), sg.Push()],
            [sg.Push(), sg.Cancel('Retornar'), sg.Push()]
        ]
        self.__window = sg.Window('Menu da Loja').Layout(layout)

    def solicitar_genero(self):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text('Digite o Gênero:', font=("Verdana",15))],
            [sg.InputText('', key='gen')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        genero = values['gen']

        self.close()
        return genero

    def solicitar_desenvolvedora(self):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text('Nome da Desenvolvedora:', font=("Verdana",12))],
            [sg.InputText('', key='dev')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        desenvolvedora = values['dev']

        self.close()
        return desenvolvedora

    def solicitar_faixa_preco(self):
        sg.ChangeLookAndFeel('DarkGray16')
        layout = [
            [sg.Text('Faixa de preço', font=("Verdana",20), colors='Cyan')],
            [sg.Text('Min:', font=("Verdana",12)), sg.InputText('', key='min')],
            [sg.Text('Max:', font=("Verdana",12)), sg.InputText('', key='max')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Jogos').Layout(layout)

        button, values = self.open()
        minimo = values['min']
        maximo = values['max']

        self.close()
        return minimo, maximo

    def exibir_lista_jogos(self, mensagem, jogos):
        sg.ChangeLookAndFeel('DarkGray16')
        jogos_layout = [
            [sg.Text(f"{jogo['nome']} - R$: {jogo['preco']}", font=("Helvetica", 12))]
            for jogo in jogos
        ]

        layout = [
            [sg.Text(mensagem,  font=("Verdana",20), colors='Cyan')],
            [sg.Column(jogos_layout)],
            [sg.Button('Comprar', button_color='Green')]
        ]
        self.__window = sg.Window('Tela de Jogos').Layout(layout)

        button, values = self.open()

        self.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values