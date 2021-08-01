import pygame
class Settings():

    def __init__(self):

        self.background_color = (0, 0, 0)
        self.volume = .5
        self.hud_color = (255, 255, 255)
        self.menu_screen_width = 512
        self.menu_screen_height = 512
        self.menu_background_color = (255, 255, 255)
        self.game_timer = 60
        self.language = 'PT-BR'
        self.menu = [True]
        self.fullscreen = [False]
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.black = (0, 0, 0)
        self.resolution_x = 512
        self.resolution_y = 512