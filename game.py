import pygame
import settings as s
import game_functions as g
from character import Character
from enemy import Enemy
from npc_1 import first_NPC
from npc_2 import second_NPC
from npc_3 import third_NPC
#from hud import Hud
#from sound import Sound

def game():
    pygame.init()  # inicia o módulo do pygame
    pygame.mouse.set_visible(False)  # desabilita o mouse na zona do jogo
    #pygame.mixer.init()  # inicia o mixer de áudio
    clock = pygame.time.Clock()  # inicia o módulo Clock
    font = pygame.font.SysFont(None, 16)  # define a fonte dos textos
    font_fps = pygame.font.SysFont(None, 16)  # define a fonte do fps
    font_timer = pygame.font.SysFont(None, 12)  # define a fonte do timer
    config = s.Settings()  # importa o arquivo settings
    fullscreen = False
    pygame.display.set_caption("Escape from Obama's Alien")  # define o título da janela
    game_screen = g.game_screen(config, fullscreen)  # chama a tela
    character = Character(game_screen)  # chama o personagem
    enemy = Enemy(game_screen, character)  # chama o inimigo
    f_npc = first_NPC(game_screen)  # chama o primeiro NPC
    s_npc = second_NPC(game_screen)  # chama o segundo NPC
    t_npc = third_NPC(game_screen)  # chama o terceiro NPC
    #sound = Sound(config)  # chama o som do jogo
    enemy_dialogue = enemy.cont_dialogue
    game_timer = 60
    while True:
        clock.tick(60)
        #game_hud = Hud(config, game_screen)
        game_timer = g.timer(clock, game_timer)
        collision_enemy = g.update_game_screen(config, game_screen, character, enemy, font, clock, font_fps, game_timer, font_timer, f_npc, s_npc, t_npc)
        g.get_event(config, game_screen, character, enemy, fullscreen, collision_enemy)
        character.update(config)
        enemy.update(config, character, game_timer)
        enemy.dialogue(enemy_dialogue)

