import pygame

white = (255, 255, 255)
black = (0, 0 , 0)

class Hud:
    #def __init__(self, config, game_screen):
    def draw_lines(self, game_screen):
        pygame.draw.line(game_screen, white, (196, 485), (280, 485))  # desenha a linha horizontal
        pygame.draw.line(game_screen, white, (196, 485), (196, 512))  # desenha a haste direita
        pygame.draw.line(game_screen, white, (280, 512), (280, 485))  # desenha a haste esquerda
        # pygame.draw.line(game_screen, white, (0, 256), (512, 256))
        # pygame.draw.line(game_screen, white, (256, 0), (256, 512)

