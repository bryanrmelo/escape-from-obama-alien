import pygame
from random import randint

class Sound:

    def __init__(self, config):
        self.background_music = 'musics/01.wav'
        self.dialogue = 'musics/03.wav'


    def play_background(self, config):
        self.background_music = pygame.mixer.music.load(self.background_music)
        self.loop = pygame.mixer.music.play(loops=- 1)
        self.volume = pygame.mixer.music.set_volume(config.volume)


    def play_dialogue(self, config):
        self.dialogue = pygame.mixer.music.load(self.dialogue)
        self.loop = pygame.mixer.music.play(loops=- 1)
        self.volume = pygame.mixer.music.set_volume(config.volume)

