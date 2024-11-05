class AmigoRepetidoError(Exception):
    def __init__(self, nick_amigo):
        self.mensagem = "O usuário {} já está em sua lista de amigos"
        super().__init__(self.mensagem.format(nick_amigo))