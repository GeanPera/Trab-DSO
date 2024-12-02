class DadoJaUtilizadoError(Exception):
    def __init__(self, nick_amigo):
        self.mensagem = "{}"
        super().__init__(self.mensagem.format(nick_amigo))