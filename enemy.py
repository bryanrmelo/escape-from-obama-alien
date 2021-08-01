import pygame
from random import randint


class Enemy:
    def __init__(self, game_screen, character):  # inicializa o módulo do inimigo

        # atribuindo funções para o resto do código

        self.cont_dialogue = 1
        self.velocity = 4
        self.dialogue_text = ''
        self.game_screen = game_screen
        self.character = character

        #  atribuindo utilidades a funções

        self.image = pygame.image.load('images/enemy/3.png')  # importar a imagem
        self.rect = self.image.get_rect()  # cria o retangulo do tamanho da imagem
        self.rect_screen = game_screen.get_rect()  # cria o retangulo na tela
        self.rect.centerx = self.rect_screen.centerx  # definir a posição x do inimigo
        self.rect.centery = self.rect_screen.centery  # definir a posição y do inimigo
        self.counter_center = randint(1, 4)
        if self.counter_center == 1:
            self.rect.centerx = 0
            self.rect.centery = 0
        if self.counter_center == 2:
            self.rect.centerx = 512
            self.rect.centery = 512
        if self.counter_center == 3:
            self.rect.centerx = 512
            self.rect.centery = 0
        if self.counter_center == 4:
            self.rect.centerx = 0
            self.rect.centery = 512


    def draw(self):  # desenhar o inimigo na tela

        self.game_screen.blit(self.image, self.rect)  # desenha o inimigo na tela conforme imagem e tamanho do retangulo

    def update(self, config, character, game_timer):  # atualizar conforme os movimentos
        if game_timer < 0:
            if self.rect.right < config.resolution_x and self.rect.x < character.rect.x:  # movimento para direita
                self.rect.x += self.velocity
                self.image = pygame.image.load('images/enemy/1.png')

            if self.rect.left > 0 and self.rect.x > character.rect.x:  # movimento para esquerda
                self.rect.x -= self.velocity
                self.image = pygame.image.load('images/enemy/2.png')


            if self.rect.bottom < config.resolution_y and self.rect.y < character.rect.y:  # movimento para baixo
                self.rect.y += self.velocity
                self.image = pygame.image.load('images/enemy/3.png')

            if self.rect.top > 0 and self.rect.y > character.rect.y:  # movimento para cima
                self.rect.y -= self.velocity
                self.image = pygame.image.load('images/enemy/4.png')

