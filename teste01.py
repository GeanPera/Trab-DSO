import unittest
from controladorJogos import ControladorJogos
from jogo import Jogo

class TestControladorJogos(unittest.TestCase):

    def setUp(self):
        # Inicializando o controlador e adicionando alguns jogos
        self.controlador = ControladorJogos()
        self.controlador.novo_jogo("The Legend of Zelda", "Aventura", "Nintendo", 12, "Aventura épica", 59.99, 1000)
        self.controlador.novo_jogo("Super Mario", "Plataforma", "Nintendo", 7, "Jogo clássico", 39.99, 1500)
        self.controlador.novo_jogo("Final Fantasy", "RPG", "Square Enix", 16, "RPG envolvente", 69.99, 500)

    def test_novo_jogo(self):
        # Verifica se o jogo foi adicionado corretamente
        self.controlador.novo_jogo("Cyberpunk 2077", "Ação", "CD Projekt Red", 18, "Futurístico", 199.99, 2000)
        self.assertEqual(len(self.controlador._ControladorJogos__jogos), 4)
        self.assertEqual(self.controlador._ControladorJogos__jogos[-1].titulo, "Cyberpunk 2077")

    def test_jogo_mais_comprado(self):
        # Verifica se o jogo mais comprado é o correto (Super Mario)
        jogo = self.controlador.jogo_mais_comprado()
        self.assertEqual(jogo.titulo, "Super Mario")
        self.assertEqual(jogo.qnt_vendida, 1500)

    def test_jogos_por_genero(self):
        # Verifica se os jogos do gênero 'RPG' são filtrados corretamente
        rpg_games = self.controlador.jogos_por_genero("RPG")
        self.assertEqual(len(rpg_games), 1)
        self.assertEqual(rpg_games[0].titulo, "Final Fantasy")

        # Verifica se não retorna jogos para um gênero que não existe
        estrategia_games = self.controlador.jogos_por_genero("Estratégia")
        self.assertEqual(len(estrategia_games), 0)

    def test_jogos_por_desenvolvedora(self):
        # Verifica se os jogos da desenvolvedora 'Nintendo' são filtrados corretamente
        nintendo_games = self.controlador.jogos_por_desenvolvedora("Nintendo")
        self.assertEqual(len(nintendo_games), 2)
        self.assertEqual(nintendo_games[0].titulo, "The Legend of Zelda")
        self.assertEqual(nintendo_games[1].titulo, "Super Mario")

        # Verifica se não retorna jogos para uma desenvolvedora que não existe
        sony_games = self.controlador.jogos_por_desenvolvedora("Sony")
        self.assertEqual(len(sony_games), 0)

    def test_filtrar_preco(self):
        # Verifica se os jogos entre 50 e 70 reais são filtrados corretamente
        jogos_filtrados = self.controlador.filtrar_preco(50, 70)
        self.assertEqual(len(jogos_filtrados), 2)  # Zelda e Final Fantasy
        self.assertEqual(jogos_filtrados[0].titulo, "The Legend of Zelda")
        self.assertEqual(jogos_filtrados[1].titulo, "Final Fantasy")

        # Verifica se não retorna jogos para uma faixa de preço sem correspondência
        jogos_inexistentes = self.controlador.filtrar_preco(500, 1000)
        self.assertEqual(len(jogos_inexistentes), 0)

if __name__ == '__main__':
    unittest.main()
