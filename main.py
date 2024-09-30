from biblioteca import Biblioteca
from jogo import Jogo
from loja import Loja
from perfil import Perfil
from pessoa import Pessoa
from usuario import Usuario
from desenvolvedora import Desenvolvedora

#Instanciando Jogadores
jogador1 = Usuario("Luan", "Cellmander", 22, "luan@123", "rua 1", "senha123", "321")
jogador2 = Usuario("Gean", "PeraGamer", 18, "gean@123", "rua vrau", "senha456", "654")

#Instanciando desenvolvedora
supercell = Desenvolvedora("Supercell")
riot = Desenvolvedora("Riot Games")

#Instanciando Jogo
brawl = Jogo("Brawl Stars", "MOBA", supercell, 0, "Brawlzada dos cria", 10, 12)
lol = Jogo("League of Legends", "MOBA", riot, 12, "Pior jogo do mundo", 25, 30)
valorant = Jogo("Valorant", "FPS", riot, 12, "Um cs com poderzinho", 15, 51)

#Depósito de saldo
jogador1.perfil.depositar_saldo(50)
jogador2.perfil.depositar_saldo(50)

#Adicionar e remover amigo
jogador1.perfil.adicionar_amigo(jogador2)
jogador1.perfil.remover_amigo(jogador2)

#Comprando jogo
brawl.comprar(jogador1)

#Presenteando um amigo
brawl.presentear_amigo(jogador1, jogador2)

#Jogando um jogo
jogador1.biblioteca.jogar(brawl)

#Jogando com amigo
jogador1.biblioteca.jogar_junto(brawl, jogador2)

#Removendo jogo da biblioteca
jogador1.biblioteca.remover_jogo(brawl)

#Obtendo lista de jogos disponíveis na loja
jogos = Loja.listar_jogos()
print(jogos)

#Lista de jogos lançados por desenvolvedora
print(supercell.listar_jogos())
print(riot.listar_jogos())

#Faturamento da desenvolvedora
faturamento1 = supercell.faturamento()
faturamento2 = riot.faturamento()
print(f"{supercell.nome}: {faturamento1}, {riot.nome}: {faturamento2}")