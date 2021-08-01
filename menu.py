import pygame
import time

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((512, 512))
        self.white_cyan = False
        self.cyan_blue = False
        self.blue_pink = False
        self.pink_red = False
        self.red_yellow = False
        self.yellow_green = False
        self.r = 255
        self.g = 255
        self.b = 255

    def draw(self, font, black, language):
        if language == 'PT-BR':
            self.screen.fill((255, 255, 255))
            self.screen.blit(font.render('Escape from Obama`s Alien', True, black), [128, 100])
            self.screen.blit(font.render('Jogar (Espaço)', True, black), [128, 195])
            self.screen.blit(font.render('Sobre (A)', True, black), [128, 230])
            self.screen.blit(font.render('Opções (O)', True, black), [128, 260])
            self.screen.blit(font.render('Sair do jogo (Q)' , True, black), [128, 290])

            pygame.draw.line(self.screen, black, (110, 130), (110, 90))  # linha vertical da esquerda (frase 1 PT)
            pygame.draw.line(self.screen, black, (410, 90), (410, 130))  # linha vertical da direita (frase 1 PT)
            pygame.draw.line(self.screen, black, (110, 90), (410, 90))  # linha horizontal de cima (frase 1 PT)
            pygame.draw.line(self.screen, black, (110, 130), (410, 130))  # linha horizontal de baixo (frase 1 PT)

            pygame.draw.line(self.screen, black, (110, 190), (110, 320))  # linha vertical da esquerda (frase 2-5 PT)
            pygame.draw.line(self.screen, black, (285, 190), (285, 320))  # linha vertical da direita (frase 2-5 PT)

            pygame.draw.line(self.screen, black, (110, 190), (285, 190))  # linha horizontal de cima (frase 2 PT)
            pygame.draw.line(self.screen, black, (110, 225), (285, 225))  # linha horizontal de baixo (frase 2 PT)
            pygame.draw.line(self.screen, black, (110, 255), (285, 255))  # linha horizontal de baixo (frase 3 PT)
            pygame.draw.line(self.screen, black, (110, 285), (285, 285))  # linha horizontal de baixo (frase 4 PT)
            pygame.draw.line(self.screen, black, (110, 320), (285, 320))  # linha horizontal de baixo (frase 5 PT)
        if language == 'EN-US':
            self.screen.fill((255, 255, 255))
            self.screen.blit(font.render('Escape from Obama`s Alien', True, black), [128, 100])  # (frase 1 EN)
            self.screen.blit(font.render('Play (Space)', True, black), [128, 200])  # (frase 2 EN)
            self.screen.blit(font.render('About (A)', True, black), [128, 230])  # (frase 3 EN)
            self.screen.blit(font.render('Options (O)', True, black), [128, 260])  # (frase 4 EN)
            self.screen.blit(font.render('Quit game (Q)' , True, black), [128, 290])  # (frase 5 EN)

            pygame.draw.line(self.screen, black, (110, 130), (110, 90))  # linha vertical da esquerda (frase 1 EN)
            pygame.draw.line(self.screen, black, (410, 90), (410, 130))  # linha vertical da direita (frase 1 EN)
            pygame.draw.line(self.screen, black, (110, 90), (410, 90))  # linha horizontal de cima (frase 1 EN)
            pygame.draw.line(self.screen, black, (110, 130), (410, 130))  # linha horizontal de baixo (frase 1 EN)

            pygame.draw.line(self.screen, black, (110, 190), (110, 320))  # linha vertical da esquerda (frase 2-5 EN)
            pygame.draw.line(self.screen, black, (270, 190), (270, 320))  # linha vertical da direita (frase 2-5 EN)

            pygame.draw.line(self.screen, black, (110, 190), (270, 190))  # linha horizontal de cima (frase 2 EN)
            pygame.draw.line(self.screen, black, (110, 225), (270, 225))  # linha horizontal de baixo (frase 2 EN)
            pygame.draw.line(self.screen, black, (110, 255), (270, 255))  # linha horizontal de baixo (frase 3 EN)
            pygame.draw.line(self.screen, black, (110, 285), (270, 285))  # linha horizontal de baixo (frase 4 EN)
            pygame.draw.line(self.screen, black, (110, 320), (270, 320))  # linha horizontal de baixo (frase 5 EN)

        if language == 'ES':
            self.screen.fill(255, 255, 255)
            self.screen.blit(font.render('Escape from Obama`s Alein', True, black) [128, 100])
            self.screen.blit(font.render('Juegar (E'))


    def draw_about(self, font, font_menu_small, black, language):
        if language == 'PT-BR':
            self.screen.fill((255, 255, 255))
            self.screen.blit(font.render('Sobre', True, black), [225, 100])
            self.screen.blit(font_menu_small.render('Créditos:', True, black), [128, 170])
            self.screen.blit(font_menu_small.render('Bryan, Marcella e Júlia', True, black), [128, 210])
            self.screen.blit(font_menu_small.render('Data: 30/11/19', True, black), [128, 230])
            self.screen.blit(font.render('Versão: 0.01', True, black), [205, 450])
            self.screen.blit(font_menu_small.render('Voltar (V)', True, black), [220, 400])
        if language == 'EN-US':
            self.screen.fill((255, 255, 255))
            self.screen.blit(font.render('About', True, black), [225, 100])
            self.screen.blit(font_menu_small.render('Credits:' , True, black), [128, 170])
            self.screen.blit(font_menu_small.render('Bryan, Marcella e Júlia', True, black), [128, 210])
            self.screen.blit(font_menu_small.render('Date: 30/11/19', True, black), [128, 230])
            self.screen.blit(font.render('Back (B)', True, black), [220, 400])
            self.screen.blit(font.render('Version: 0.01', True, black), [205, 450])

    def draw_options(self, font, font_menu_small, black, language):

        if language == 'PT-BR':
            self.screen.fill((255, 255, 255))
            self.screen.blit(font.render('Opções', True, black), [225, 100])

            self.language_rect = pygame.draw.rect(self.screen, [255, 255, 255], [120, 200, 115, 22], 1)
            self.screen.blit(font_menu_small.render('Idioma: ' + str(language), True, black), [128, 200])

            self.resolution_rect = pygame.draw.rect(self.screen, [255, 255, 255], [120, 240, 150, 22], 1)
            self.screen.blit(font_menu_small.render('Resolução: 512x512', True, black), [128, 240])

            self.fullscreen_rect = pygame.draw.rect(self.screen, [255, 255, 255], [120, 280, 150, 22], 1)
            self.screen.blit(font_menu_small.render('Tela cheia: False', True, black), [128, 280])

            self.screen.blit(font_menu_small.render('', True, black), [128, 320])
            self.screen.blit(font.render('Voltar (V)', True, black), [205, 450])

        if language == 'EN-US':
            self.screen.fill((255, 255, 255))
            self.screen.blit(font.render('Options', True, black), [225, 100])

    def mouse_collision(self, mouse_position):
        self.mouse_rect = pygame.draw.rect(self.screen, [self.r, self.g, self.b], (mouse_position[0], mouse_position[1], 10, 10))

    '''
    def rgb(self):
        while True:
            for i in range(1):
                if self.r <= 255 and self.g == 255 and self.b == 255:
                    self.r -= 1
                    if self.r == 0:
                        self.white_cyan = True
                        self.yellow_green = False
                    # branco para azul ciano
                if self.r == 0 and self.g <= 255 and self.b == 255 and self.white_cyan == True:
                    self.g -= 1
                    if self.g == 0:
                        self.cyan_blue = True
                        self.white_cyan = False
                    # azul ciano para azul
                if self.r >= 0 and self.g == 0 and self.b == 255 and self.cyan_blue == True:
                    if self.r != 255:
                        self.r += 1
                        if self.r == 255 and self.b == 255:
                            self.blue_pink = True
                            self.cyan_blue = False
                    # azul para rosa
                if self.r <= 255 and self.g == 0 and self.b <= 255 and self.blue_pink == True:
                    self.b -= 1
                    if self.b == 0:
                        self.pink_red = True
                        self.blue_pink = False
                    # rosa para vermelho
                if self.r <= 255 and self.g >= 0 and self.b >= 0 and self.pink_red == True:
                    if self.g != 255:
                        self.g += 1
                        if self.r == 255 and self.g == 255:
                            self.red_yellow = True
                            self.pink_red = False

                    # vermelho para amarelo
                if self.r <= 255 and self.g == 255 and self.b == 0 or self.b == 1 and self.red_yellow == True:
                    self.r -= 1
                    if self.r == 0:
                        self.yellow_green = True
                        self.red_yellow = False
                    # amarelo para verde
                if self.r >= 0 and self.g == 255 and self.b >= 0 and self.yellow_green == True:
                    if self.r != 255 and self.b != 255:
                        self.r += 1
                        self.b += 1
                print(self.r, self.g, self.b)
                time.sleep(0.1)
    '''
    def game_over_screen(self, language, font, font_huge, black):
        if language == 'PT-BR':
            self.screen.fill((255, 255, 255))
            self.screen.blit(font_huge.render('Jogo finalizado', True, black), [150, 156])
            self.screen.blit(font.render('Aperte espaço para sair', True, black), [185, 320])

            pygame.draw.line(self.screen, black, (180, 317), (315, 317))
            pygame.draw.line(self.screen, black, (180, 335), (315, 335))
            pygame.draw.line(self.screen, black, (180, 317), (180, 335))
            pygame.draw.line(self.screen, black, (315, 317), (315, 335))
        if language == 'EN-US':
            self.screen.fill ((255, 255, 255))
            self.screen.blit(font_huge.render('Game over', True, black), [170, 156])
            self.screen.blit(font.render('Press space to leave', True, black), [190, 320])
            pygame.draw.line(self.screen, black, (180, 317), (315, 317))
            pygame.draw.line(self.screen, black, (180, 335), (315, 335))
            pygame.draw.line(self.screen, black, (180, 317), (180, 335))
            pygame.draw.line(self.screen, black, (315, 317), (315, 335))