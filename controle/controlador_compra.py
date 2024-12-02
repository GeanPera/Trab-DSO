from limite.tela_compra import TelaCompra


class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_compra = TelaCompra()

    def comprar(self, jogo):
        jogo_escolhido = self.__controlador_sistema.controlador_jogos.jogo(jogo)
        try:
            nickname = self.__tela_compra.pede_nickname("Qual seu Nickname? ")
            usuario = self.__controlador_sistema.controlador_usuarios.encontrar_usuario(nickname)
            if not usuario:
                raise AttributeError("Usuário não encontrado.")

            senha = self.__tela_compra.pede_senha()
            if usuario.senha != senha:
                raise ValueError("Senha incorreta!")

            if usuario.saldo < jogo_escolhido.preco:
                raise ValueError("Saldo insuficiente!")

            if usuario.idade < jogo_escolhido.faixa_etaria:
                raise ValueError("Você não possui idade suficiente para comprar esse jogo!")

            jogo_adicionado = self.__controlador_sistema.controlador_usuarios.adicionar_jogo(jogo_escolhido, usuario)

            if jogo_adicionado is None:
                self.__tela_compra.mostra_mensagem(f"Você já possui este jogo!")
                return
            self.__tela_compra.mostra_mensagem(f"Compra realizada com sucesso. Saldo atual: {usuario.saldo}")
        except AttributeError as e:
            self.__tela_compra.mostra_mensagem(str(e))
        except ValueError as e:
            self.__tela_compra.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_compra.mostra_mensagem(f"Erro inesperado ao comprar: {str(e)}")

    def presentear(self, jogo):
        jogo_escolhido = self.__controlador_sistema.controlador_jogos.jogo(jogo)

        if not jogo_escolhido:
            raise AttributeError("Jogo não encontrado.")

        try:
            my_nickname = self.__tela_compra.pede_nickname("Qual seu Nickname? ")
            usuario = self.__controlador_sistema.controlador_usuarios.encontrar_usuario(my_nickname)
            if not usuario:
                raise AttributeError("Usuário não encontrado.")
            
            senha = self.__tela_compra.pede_senha()
            if usuario.senha != senha:
                raise ValueError("Senha incorreta!")

            amigo_nickname = self.__tela_compra.pede_nickname("Qual o Nickname do seu amigo? ")
            amigo = self.__controlador_sistema.controlador_usuarios.encontrar_usuario(amigo_nickname)
            if not amigo:
                raise AttributeError("Amigo não encontrado.")

            if usuario.saldo < jogo_escolhido.preco:
                raise ValueError("Saldo insuficiente!")

            if amigo.idade < jogo_escolhido.faixa_etaria:
                raise ValueError(f"{amigo.nickname} não possui idade suficiente para receber esse jogo!")

            self.__controlador_sistema.controlador_usuarios.presentear_amigo(jogo_escolhido, amigo, usuario)
            self.__tela_compra.mostra_mensagem(f"Presente enviado com sucesso. Saldo atual: {usuario.saldo}")

        except AttributeError as e:
            self.__tela_compra.mostra_mensagem(str(e))
        except ValueError as e:
            self.__tela_compra.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_compra.mostra_mensagem(f"Erro inesperado ao presentear: {str(e)}")

    def abre_tela(self, jogo):
        jogo_escolhido = self.__controlador_sistema.controlador_jogos.jogo(jogo)
        while True:
            opcao_escolhida = self.__tela_compra.opcao_compra(jogo_escolhido)
            if opcao_escolhida == 1:
                self.comprar(jogo)
            if opcao_escolhida == 2:
                self.presentear(jogo)
            if opcao_escolhida == 0:
                return
