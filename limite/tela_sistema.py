import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()
        
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

            
    def close(self):
        self.__window.Close()
                
    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('SIN Games', font=("Verdana", 25, ), colors='Cyan')],
            [sg.Text('Escolha uma opção!', font=("Verdana", 18))],
            [sg.Radio('Menu Loja', 'RD1', key ='1')],
            [sg.Radio('Usuário', 'RD1', key ='2')],
            [sg.Radio('Relatório', 'RD1', key='3')],
            [sg.Button('Confirmar', button_color='Green'), sg.Cancel('Encerrar sessão', button_color='Red')]
        ]
        self.__window = sg.Window('SIN Games').Layout(layout)

    def mostra_mensagem(self, mensagem):
        print(f"{mensagem}")