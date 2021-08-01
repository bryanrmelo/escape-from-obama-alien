import pygame

class first_NPC:
    def __init__(self, game_screen):
        self.cont_dialogue = 1
        self.game_screen = game_screen
        self.image = pygame.image.load('images/npc1.png')
        self.rect = self.image.get_rect()
        self.rect_screen = game_screen.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 100
        self.dialogue_text = ''
        self.image_item = pygame.image.load('images/item1.png')
        self.rect_item = self.image_item.get_rect()
        self.rect_item.centerx = 200
        self.rect_item.centery = 250

    def draw(self):
        self.game_screen.blit(self.image, self.rect)



    def dialogue(self):
        if self.cont_dialogue == 1:
            self.dialogue_text = 'Olá'
        elif self.cont_dialogue == 2:
            self.dialogue_text = 'Mundo'

    def item(self):
        self.game_screen.blit(self.image_item, self.rect_item)
