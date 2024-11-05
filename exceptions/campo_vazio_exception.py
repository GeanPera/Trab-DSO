class CamposVaziosError(Exception):
    def __init__(self, mensagem="Todos os campos devem ser preenchidos."):
        super().__init__(mensagem)