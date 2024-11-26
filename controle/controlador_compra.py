from limite.tela_compra import TelaCompra


class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_compra = TelaCompra()

    def comprar(self):
        try:
            nome_jogo = self.__tela_compra.solicitar_jogo("Nome do jogo que deseja comprar?  ")
            jogo_escolhido = self.__controlador_sistema.controlador_jogos.jogo(nome_jogo)

            if not jogo_escolhido:
                raise AttributeError("Jogo não encontrado.")

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

                self.__controlador_sistema.controlador_usuarios.adicionar_jogo(jogo_escolhido, usuario)
                self.__tela_compra.mostra_mensagem(f"Compra realizada com sucesso. Saldo atual: {usuario.saldo}")
            except AttributeError as e:
                self.__tela_compra.mostra_mensagem(str(e))
            except ValueError as e:
                self.__tela_compra.mostra_mensagem(str(e))
            except Exception as e:
                self.__tela_compra.mostra_mensagem(f"Erro inesperado ao comprar: {str(e)}")
        except AttributeError as e:
            self.__tela_compra.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_compra.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def presentear(self):
        try:
            nome_jogo = self.__tela_compra.solicitar_jogo("Nome do jogo que deseja comprar? ")
            jogo_escolhido = self.__controlador_sistema.controlador_jogos.jogo(nome_jogo)

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

                # Presentear o amigo caso todas as condições sejam atendidas
                self.__controlador_sistema.controlador_usuarios.presentear_amigo(jogo_escolhido, amigo, usuario)
                self.__tela_compra.mostra_mensagem(f"Presente enviado com sucesso. Saldo atual: {usuario.saldo}")

            except AttributeError as e:
                self.__tela_compra.mostra_mensagem(str(e))
            except ValueError as e:
                self.__tela_compra.mostra_mensagem(str(e))
            except Exception as e:
                self.__tela_compra.mostra_mensagem(f"Erro inesperado ao presentear: {str(e)}")

        except AttributeError as e:
            self.__tela_compra.mostra_mensagem(str(e))
        except Exception as e:
            self.__tela_compra.mostra_mensagem(f"Erro inesperado: {str(e)}")

    def voltar(self):
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