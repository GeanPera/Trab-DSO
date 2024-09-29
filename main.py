from biblioteca import Biblioteca
from jogo import Jogo
from loja import Loja
from perfil import Perfil
from pessoa import Pessoa
from usuario import Usuario

#Instanciando Jogadores
jogador1 = Usuario("Luan", "Cellmander", 22, "luan@123", "rua 1", "senha123", "321")
jogador2 = Usuario("Gean", "PeraGamer", 18, "gean@123", "rua vrau", "senha456", "654")

#Instanciando Jogo
brawl = Jogo("Brawl Stars", "MOBA", "Supercell", 0, "Brawlzada dos cria", 10, 12)

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
