import pygame


class Character:

    def __init__(self, game_screen):
        self.velocity = 3
        self.game_screen = game_screen
        self.image = pygame.image.load('images/character/3.png')
        self.rect = self.image.get_rect()
        self.rect_screen = game_screen.get_rect()
        self.rect.centerx = 256
        self.rect.centery = 256
        self.move_right = False
        self.move_left = False
        self.move_down = False
        self.move_up = False

    def draw(self):  # desenhar o inimigo na tela
        self.game_screen.blit(self.image, self.rect)

    def update(self, config):
        if self.move_right and self.rect.right < config.resolution_x:
            self.rect.x += self.velocity
            self.image = pygame.image.load('images/character/1.png')

        if self.move_left and self.rect.left > 0:
            self.rect.x -= self.velocity
            self.image = pygame.image.load('images/character/2.png')

        if self.move_down and self.rect.bottom < config.resolution_y:
            self.rect.y += self.velocity
            self.image = pygame.image.load('images/character/3.png')

        if self.move_up and self.rect.top > 0:
            self.rect.y -= self.velocity
            self.image = pygame.image.load('images/character/4.png')
