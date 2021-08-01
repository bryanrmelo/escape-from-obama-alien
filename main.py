import pygame
import settings as s
import game_functions as g
from character import Character
from enemy import Enemy
from npc_1 import first_NPC
from npc_2 import second_NPC
from npc_3 import third_NPC
from hud import Hud
from menu import Menu
from boss import Boss
#from sound import Sound

def main():
    pygame.init()  # inicia o módulo do pygame
    #pygame.event.set_grab(True)
    #pygame.mixer.init()  # inicia o mixer de áudio
    clock = pygame.time.Clock()  # inicia o módulo Clock
    font = pygame.font.SysFont(None, 16)  # define a fonte dos textos
    font_fps = pygame.font.SysFont(None, 16)  # define a fonte do fps
    font_timer = pygame.font.SysFont(None, 12)  # define a fonte do timer
    font_menu_play = pygame.font.SysFont(None, 30)
    font_menu_small = pygame.font.SysFont(None, 22)
    font_huge = pygame.font.SysFont(None, 44)
    config = s.Settings()  # importa o arquivo settings
    fullscreen = config.fullscreen  # define a variavel de tela cheia como falsa
    pygame.display.set_caption("Escape from Obama's Alien")  # define o título da janela
    game_screen = g.game_screen(config, fullscreen)  # chama a tela
    character = Character(game_screen)  # chama o personagem
    enemy = Enemy(game_screen, character)  # chama o inimigo
    f_npc = first_NPC(game_screen)  # chama o primeiro NPC
    s_npc = second_NPC(game_screen)  # chama o segundo NPC
    t_npc = third_NPC(game_screen)  # chama o terceiro NPC
    game_hud = Hud()
    main_menu = Menu()
    #sound = Sound(config)  # chama o som do jogo
    game_timer = config.game_timer
    language = config.language
    menu = config.menu
    menu_about_draw = [False]
    menu_options_draw = [False]
    game_over_screen = [False]
    white = config.white
    black = config.black
    green = config.green
    draw_item = [False,False,False]
    hud_item = [False, False, False]
    boss = Boss(game_screen)
    while True:
        clock.tick(60)
        if not menu[0]:
            game_timer = g.timer(clock, game_timer)
        if menu[0]:
            mouse_position = pygame.mouse.get_pos()
        collision_enemy = g.update_screen(main_menu, menu, font_menu_play, config, game_screen, character, enemy, font, clock, font_fps, game_timer,
                                          font_timer, f_npc, s_npc, t_npc, game_hud, menu_about_draw, language, font_menu_small, black, white, green,
                                          menu_options_draw, mouse_position, game_over_screen, font_huge, draw_item, hud_item, boss)
        g.get_event(menu, main_menu, config, game_screen, character, enemy, fullscreen, collision_enemy, font, menu_about_draw, language, menu_options_draw, f_npc, s_npc, t_npc, game_over_screen, draw_item, hud_item, game_timer)
        character.update(config)
        enemy.update(config, character, game_timer)
        f_npc.dialogue()
        s_npc.dialogue()
        t_npc.dialogue()

main()