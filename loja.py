
class Loja():

    jogos_disponiveis = []
    
 
    
    @classmethod
    def novo_jogo(cls, Jogo):
        cls.jogos_disponiveis.append(Jogo)

    @classmethod
    def listar_jogos(cls):
        return [jogo.titulo for jogo in cls.jogos_disponiveis]


    def jogo_mais_comprado(self):
        pass

    def jogos_por_genero(self):
        pass

    def jogos_por_desenvolvedora(self):
        pass

    def filtro_preco(self):
        pass
