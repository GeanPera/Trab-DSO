class UsuarioNaoEncontradoError(Exception):
    def __init__(self, mensagem="Usuário não encontrado."):
        super().__init__(mensagem)