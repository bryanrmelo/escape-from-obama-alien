import pygame
import time
from random import randint

class Boss:
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.image = pygame.image.load('images/boss.png')
        self.rect = self.image.get_rect()
        self.rect_screen = game_screen.get_rect()
        self.rect.centerx = 50
        self.rect.centery = 50
        self.dialogue_text = ''

    def draw(self, cam):
        self.game_screen.blit(self.image,self.rect)


