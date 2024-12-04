import pygame

class JogoBrickBreaker:
    def __init__(self):

        pygame.init()
        self.tamanho_tela = (800, 800)
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        pygame.display.set_caption("SIN Games")
        

        self.tamanho_bola = 15
        self.bola = pygame.Rect(100, 500, self.tamanho_bola, self.tamanho_bola)
        self.tamanho_jogador = 100
        self.jogador = pygame.Rect(0, 750, self.tamanho_jogador, 15)
        

        self.qtde_blocos_linha = 8
        self.qtde_linhas_blocos = 5
        self.qtde_total_blocos = self.qtde_blocos_linha * self.qtde_linhas_blocos
        self.blocos = self.criar_blocos(self.qtde_blocos_linha, self.qtde_linhas_blocos)

        self.cores = {
            "branca": (255, 255, 255),
            "preta": (0, 0, 0),
            "amarela": (255, 255, 0),
            "azul": (0, 0, 255),
            "verde": (0, 255, 0)
        }

        self.fim_jogo = False
        self.pontuacao = 0

        self.movimento_bola = [1, -1]

    def criar_blocos(self, qtde_blocos_linha, qtde_linhas_blocos):
        altura_tela = self.tamanho_tela[1]
        largura_tela = self.tamanho_tela[0]
        distancia_entre_blocos = 5
        largura_bloco = largura_tela / 8 - distancia_entre_blocos
        altura_bloco = 15
        distancia_entre_linhas = altura_bloco + 10
        blocos = []

        for j in range(qtde_linhas_blocos):
            for i in range(qtde_blocos_linha):

                bloco = pygame.Rect(i * (largura_bloco + distancia_entre_blocos), j * distancia_entre_linhas, largura_bloco, altura_bloco)

                blocos.append(bloco)
        return blocos

    def desenhar_inicio_jogo(self):
        self.tela.fill(self.cores["preta"])
        pygame.draw.rect(self.tela, self.cores["azul"], self.jogador)
        pygame.draw.rect(self.tela, self.cores["branca"], self.bola)

    def desenhar_blocos(self):
        for bloco in self.blocos:
            pygame.draw.rect(self.tela, self.cores["verde"], bloco)

    def movimentar_jogador(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                if (self.jogador.x + self.tamanho_jogador) < self.tamanho_tela[0]:
                    self.jogador.x = self.jogador.x + 50
            if evento.key == pygame.K_LEFT:
                if self.jogador.x > 0:
                    self.jogador.x = self.jogador.x - 50

    def movimentar_bola(self):
        movimento = self.movimento_bola
        self.bola.x = self.bola.x + movimento[0]
        self.bola.y = self.bola.y + movimento[1]

        if self.bola.x <= 0:
            movimento[0] = - movimento[0]
        if self.bola.y <= 0:
            movimento[1] = - movimento[1]
        if self.bola.x + self.tamanho_bola >= self.tamanho_tela[0]:
            movimento[0] = - movimento[0]
        if self.bola.y + self.tamanho_bola >= self.tamanho_tela[1]:
            movimento = None

        if self.jogador.collidepoint(self.bola.x, self.bola.y):
            movimento[1] = - movimento[1]

        # Verificar colisão com os blocos
        for bloco in self.blocos:
            if bloco.collidepoint(self.bola.x, self.bola.y):
                self.blocos.remove(bloco)
                movimento[1] = - movimento[1]

        return movimento

    def atualizar_pontuacao(self):
        fonte = pygame.font.Font(None, 30)
        texto = fonte.render(f"Pontuação: {self.qtde_total_blocos - len(self.blocos)}", 1, self.cores["amarela"])
        self.tela.blit(texto, (0, 780))

        # Verificar se todos os blocos foram destruídos
        if len(self.blocos) == 0:
            return True
        else:
            return False

    def loop_jogo(self):
        while not self.fim_jogo:
            self.desenhar_inicio_jogo()
            self.desenhar_blocos()

            # Atualizar a pontuação
            if self.atualizar_pontuacao():
                self.fim_jogo = True

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.fim_jogo = True
                self.movimentar_jogador(evento)

            self.movimento_bola = self.movimentar_bola()

            # Verificar se a bola saiu da tela
            if self.movimento_bola is None:
                self.fim_jogo = True

            pygame.time.wait(1)
            pygame.display.flip()

        pygame.quit()
