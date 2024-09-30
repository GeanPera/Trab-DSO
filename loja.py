

class Loja():

    jogos_disponiveis = []
    
 
    
    @classmethod
    def novo_jogo(cls, Jogo):
        cls.jogos_disponiveis.append(Jogo)

    @classmethod
    def listar_jogos(cls):
        return [jogo.titulo for jogo in cls.jogos_disponiveis]

    @classmethod
    def jogo_mais_comprado(cls):
        if not cls.jogos_disponiveis:
            return "Não há jogos na loja."
        jogo_mais_vendido = max(cls.jogos_disponiveis, key=lambda jogo: jogo.qntd_vendida)
        return f"{jogo_mais_vendido.titulo} é o jogo mais comprado atualmente."

    def jogos_por_genero(self):
        pass

    @classmethod
    def jogos_por_desenvolvedora(cls, desenvolvedora):
        jogos = [jogo.titulo for jogo in cls.jogos_disponiveis if jogo.desenvolvedora == desenvolvedora]
        if jogos:
            return f"Jogos da {desenvolvedora.nome}: {', '.join(jogos)}"
        else:
            return f"A desenvolvedora {desenvolvedora.nome} não tem jogos registrados."
        
    def filtro_preco(self):
        pass
