import pygame
pygame.init()

#Define o tamanho da janela.
WIDTH, HEIGHT = 700, 500
janela = pygame.display.set_mode((WIDTH, HEIGHT))

#Coloca um nome a janela.
pygame.display.set_caption("Pong")


FPS = 60
clock = pygame.time.Clock()

#Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FIGURA_WIDTH, FIGURA_HEIGHT= 20, 100

class Figura:
    COLOR = WHITE

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self. width = width
        self.height = height

    def draw(self, janela):
        pygame.draw.rect(janela, self.COLOR, (self.x, self. y, self.width, self.height))


#Desenha na janela do jogo
def draw(janela, figuras):
    janela.fill(BLACK)

    for figura in figuras:
        figura.draw(janela)

    pygame.display.update()


def main():
    
    rodando = True

    figura_equerda = Figura(10, HEIGHT//2 - FIGURA_HEIGHT//2, FIGURA_WIDTH, FIGURA_HEIGHT)
    figura_direita = Figura(WIDTH - 10 - FIGURA_WIDTH, HEIGHT//2 - FIGURA_HEIGHT//2, FIGURA_WIDTH, FIGURA_HEIGHT)
    

    while rodando:
        
        #Atualiza o FPS
        clock.tick(FPS)
        draw(janela[figura_equerda, figura_direita])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                break
    
    pygame.quit()

if __name__ == '__main__':
    main()