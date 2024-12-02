class UsuarioNaoEncontradoError(Exception):
    def __init__(self, mensagem="Usuário nao encontrado."):
        super().__init__(mensagem)