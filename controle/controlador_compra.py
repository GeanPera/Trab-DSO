from limite.tela_compra import TelaCompra


class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_compra = TelaCompra()

    def comprar(self):
        nome_jogo = self.__tela_compra.solicitar_jogo("Nome do jogo que deseja comprar?  ")
        jogo_escolhido = self.__controlador_sistema.controlador_jogos.jogo(nome_jogo)
        nickname = self.__tela_compra.pede_nickname("Qual seu Nickname? ")
        usuario = self.__controlador_sistema.controlador_usuarios.encontrar_usuario(nickname)

        if jogo_escolhido:
            if usuario:
                if usuario.saldo >= jogo_escolhido.preco and usuario.idade >= jogo_escolhido.faixa_etaria:
                    self.__controlador_sistema.controlador_usuarios.adicionar_jogo(jogo_escolhido, usuario)
                    self.__tela_compra.mostra_mensagem(f"Compra realizada com sucesso. Saldo atual: {usuario.saldo}")
            else:
                self.__tela_compra.mostra_mensagem("Usuário não encontrado.")            
        else:
            self.__tela_compra.mostra_mensagem("Jogo não encontrado.")

    def presentear(self):
        nome_jogo = self.__tela_compra.solicitar_jogo("Nome do jogo que deseja comprar?  ")
        jogo_escolhido = self.__controlador_sistema.controlador_jogos.jogo(nome_jogo)
        my_nickname = self.__tela_compra.pede_nickname("Qual seu Nickname? ")
        usuario = self.__controlador_sistema.controlador_usuarios.encontrar_usuario(my_nickname)
        amigo_nickname = self.__tela_compra.mostra_mensagem("Qual o Nickname do seu amigo? ")
        amigo = self.__controlador_sistema.controlador_usuarios.encontrar_usuario(amigo_nickname)
        if jogo_escolhido:
            if usuario:
                if amigo:
                    if usuario.saldo >= jogo_escolhido.preco:
                        self.__controlador_sistema.controlador_usuarios.presentear_amigo(jogo_escolhido, amigo, usuario)
                        self.__tela_compra.mostra_mensagem(f"Presente enviado com sucesso. Saldo atual: {usuario.saldo}")
                else:
                    self.__tela_compra.mostra_mensagem("Amigo não encontrado.")
            else:
                self.__tela_compra.mostra_mensagem("Usuário não encontrado.")            
        else:
            self.__tela_compra.mostra_mensagem("Jogo não encontrado.")
    def voltar(self):
        self.__tela_compra.mostra_mensagem("Retornando...")
        return

    def abre_tela(self):
        lista_opcoes = {1: self.comprar, 2: self.presentear, 0: self.voltar}

        while True:
            opcao_escolhida = self.__tela_compra.opcao_compra()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
                if opcao_escolhida == 0:
                    break
            except KeyError:
                self.__tela_compra.mostra_mensagem("Opção inválida. Tente novamente.")