from jogo import Jogo
from loja import Loja
from usuario import Usuario
from desenvolvedora import Desenvolvedora


# Instanciando Jogadores
jogador1 = Usuario("Luan", "Cellmander", 22, "luan@123", "rua 1", "senha123", "321")
jogador2 = Usuario("Gean", "PeraGamer", 18, "gean@123", "rua vrau", "senha456", "654")

# Instanciando desenvolvedora
supercell = Desenvolvedora("Supercell")
riot = Desenvolvedora("Riot Games")

# Instanciando Jogo
brawl = Jogo("Brawl Stars", "MOBA", supercell, 0, "Brawlzada dos cria", 10, 12)
lol = Jogo("League of Legends", "MOBA", riot, 12, "Pior jogo do mundo", 25, 30)
valorant = Jogo("Valorant", "FPS", riot, 12, "Um cs com poderzinho", 15, 51)

# Depósito de saldo
jogador1.perfil.depositar_saldo(50)


# Comprando jogo
brawl.comprar(jogador1)
lol.comprar(jogador1)

# Comprando um jogo repetido
brawl.comprar(jogador1)

# Mostrar jogos da biblioteca
print(jogador1.biblioteca.mostrar_biblioteca())
