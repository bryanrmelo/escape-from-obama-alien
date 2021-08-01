import sys
import pygame

    # define a tela do jogo
def game_screen(config, fullscreen):
    if fullscreen[0]:
        game_screen = pygame.display.set_mode((config.resolution_x, config.resolution_y), pygame.FULLSCREEN)
        return game_screen
    elif not fullscreen[0]:
        game_screen = pygame.display.set_mode((config.resolution_x, config.resolution_y))
        return game_screen


def get_event(menu , main_menu, config, game_screen, character, enemy, fullscreen, collision_enemy, font, menu_about_draw, language,
              menu_options_draw, f_npc, s_npc, t_npc, game_over_screen, draw_item, hud_item, game_timer):  # verifica eventos motivados pelo usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # verifica se tecla foi pressionada
        elif event.type == pygame.KEYDOWN:
            get_event_keydown(event, menu, main_menu, config, game_screen, character, enemy , fullscreen, collision_enemy, font,
                              menu_about_draw, language, menu_options_draw, f_npc, s_npc, t_npc, game_over_screen, draw_item, hud_item, game_timer)  # chama função

        # verifica se tecla foi solta
        elif event.type == pygame.KEYUP:
            get_event_keyup(event, character)  # chama função


def update_screen(main_menu, menu, font_menu_play,config, game_screen, character, enemy, font, clock, font_fps, game_timer,
                  font_timer, f_npc, s_npc, t_npc, game_hud, menu_about_draw, language, font_menu_small, black, white, green,
                  menu_options_draw, mouse_position, game_over_screen, font_huge, draw_item, hud_item, boss):  # verifica colisões e atualiza os elementos na tela
    if menu[0]:
        pygame.mouse.set_visible(True)
        main_menu.mouse_collision(mouse_position)
        if menu_about_draw[0]:
            main_menu.draw_about(font_menu_play, font_menu_small, black, language)
        elif menu_options_draw[0]:
            main_menu.draw_options(font_menu_play, font_menu_small, black, language)
        else:
            main_menu.draw(font_menu_play, black, language)
    if not menu[0]:
        pygame.mouse.set_visible(False)
        game_screen.fill(config.background_color)  # preenche a tela com a cor definida no arquivo settings
        character.draw()
        if game_timer <= 1:
            enemy.draw()
        f_npc.draw()
        s_npc.draw()
        t_npc.draw()
        if draw_item[0]:
            f_npc.item()
        if draw_item[1]:
            s_npc.item()
        if draw_item[2]:
            t_npc.item()
        game_hud.draw_lines(game_screen) # desenha as linhas do hud
        if game_over_screen[0]:
            main_menu.game_over_screen(language, font, font_huge, black)
        if hud_item[0] and hud_item[1] and hud_item[2]:
            boss.draw(game_screen)

        # mostra textos na tela
        game_screen.blit(font_timer.render('Tempo:' + str(int(game_timer)), True, white), [475, 0])  # mostra o tempo na tela
        #game_screen.blit(font_fps.render(str(int(clock.get_fps())), True, green), [0, 0])  # mostra os fps na tela

        # verifica colisões
        if character.rect.colliderect(f_npc.rect):
            game_screen.blit(font.render(f_npc.dialogue_text, True, white), [f_npc.rect.x, f_npc.rect.y - 20])
            draw_item[0] = True
        if character.rect.colliderect(s_npc.rect):
            game_screen.blit(font.render(s_npc.dialogue_text, True, white), [s_npc.rect.x, s_npc.rect.y - 20])
            draw_item[1] = True
        if character.rect.colliderect(t_npc.rect):
            game_screen.blit(font.render(t_npc.dialogue_text, True, white), [t_npc.rect.x, t_npc.rect.y - 20])
            draw_item[2] = True

        if character.rect.colliderect(f_npc.rect_item) and draw_item[0]:
            game_screen.blit(font.render('Pegar (E)', True, white), [f_npc.rect_item.x, f_npc.rect_item.y - 20])
        if character.rect.colliderect(s_npc.rect_item) and draw_item[1]:
            game_screen.blit(font.render('Pegar (E)', True, white), [s_npc.rect_item.x, s_npc.rect_item.y - 20])
        if character.rect.colliderect(t_npc.rect_item) and draw_item[2]:
            game_screen.blit(font.render('Pegar (E)', True, white), [t_npc.rect_item.x, t_npc.rect_item.y - 20])

        if character.rect.colliderect(boss.rect):
            game_over_screen[0] = True

        if enemy.rect.colliderect(character.rect):
            game_over_screen[0] = True

    pygame.display.flip()  # atualiza tela


def get_event_keydown(event, menu, main_menu, config, game_screen, character, enemy, fullscreen, collision_enemy,
                      font, menu_about_draw, language, menu_options_draw, f_npc, s_npc, t_npc, game_over_screen, draw_item, hud_item, game_timer):  # define ações para quando uma tecla for pressionada
    if menu[0]:

        # detecção de cliques no menu
        if not menu_about_draw[0]:
            if event.key == pygame.K_a:
                menu_about_draw[0] = True
        if menu_about_draw[0]:
            if language == 'PT-BR':
                if event.key == pygame.K_v:
                    menu_about_draw[0] = False
            if language == 'EN-US':
                if event.key == pygame.K_b:
                    menu_about_draw[0] = False
        if not menu_options_draw[0]:
            if event.key == pygame.K_o:
                menu_options_draw[0] = True
        if menu_options_draw[0]:
            if language == 'PT-BR':
                if event.key == pygame.K_v:
                    menu_options_draw[0] = False
            if language == 'EN-US':
                if event.key == pygame.K_b:
                    menu_options_draw[0] = False
        '''
        # detecção do mouse dentro do menu
        if event.key == pygame.mouse.get_pressed():
            mouse_click[0] = True
            print('a')
            print(mouse_click[0])
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('a')
        '''
        if event.key == pygame.K_SPACE:  # inicia o jogo
                menu[0] = False

        # comandos de saída
        if event.key == pygame.K_q:  # encerra o jogo
            sys.exit('Game ended')

    if not menu[0]:
        if not game_over_screen[0]:
            if event.key == pygame.K_ESCAPE:
                menu[0] = True

        if game_over_screen[0]:
            if event.key == pygame.K_SPACE:
                sys.exit('Game ended')

        # tela
        if event.key == pygame.K_f:  # ativa a tela-cheia do jogo
            fullscreen[0] = True
        if event.key == pygame.K_g:  # desativa a tela-cheia do jogo
            fullscreen[0] = False

        # dialogo
        if event.key == pygame.K_e and character.rect.colliderect(f_npc.rect):  # verifica o clique da tecla "E" nos diálogos
            f_npc.cont_dialogue += 1
        if event.key == pygame.K_t and character.rect.colliderect(f_npc.rect):
            f_npc.cont_dialogue -= 1
        if event.key == pygame.K_e and character.rect.colliderect(s_npc.rect):  # verifica o clique da tecla "E" nos diálogos
            s_npc.cont_dialogue += 1
        if event.key == pygame.K_t and character.rect.colliderect(s_npc.rect):
            s_npc.cont_dialogue -= 1
        if event.key == pygame.K_e and character.rect.colliderect(t_npc.rect):  # verifica o clique da tecla "E" nos diálogos
            t_npc.cont_dialogue += 1
        if event.key == pygame.K_t and character.rect.colliderect(t_npc.rect):
            t_npc.cont_dialogue -= 1

        # movimento do jogador
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # define valor True para a variável de movimento para direita do jogador
            character.move_right = True
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # define valor True para a variável de movimento para esquerda do jogador
            character.move_left = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:  # define valor True para a variável de movimento para baixo do jogador
            character.move_down = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:  # define valor True para a variável de movimento para cima do jogador
            character.move_up = True
        if event.key == pygame.K_LSHIFT:  # aumenta a variável de velocidade do jogador
            character.velocity = 10

        if event.key == pygame.K_e and draw_item[0] == True:
            f_npc.rect_item.centerx = 208
            f_npc.rect_item.centery = 496
            hud_item[0] = True
        if event.key == pygame.K_e and draw_item[1] == True:
            s_npc.rect_item.centerx = 240
            s_npc.rect_item.centery = 496
            hud_item[1] = True
        if event.key == pygame.K_e and draw_item[2] == True:
            t_npc.rect_item.centerx = 272
            t_npc.rect_item.centery = 496
            hud_item[2] = True

def get_event_keyup(event, character):  # define ações para quando uma tecla for solta
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # define valor False para a variável de movimento para direita do jogador
        character.move_right = False
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:  # define valor False para a variável de movimento para esquerda do jogador
        character.move_left = False
    if event.key == pygame.K_w or event.key == pygame.K_UP:  # define valor False para a variável de movimento para cima do jogador
        character.move_up = False
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:  # define valor False para a variável de movimento para baixo do jogador
        character.move_down = False
    if event.key == pygame.K_LSHIFT:  # diminui a variável de velocidade do jogador
        character.velocity = 1


def timer(clock, game_timer):  # cria um temporizador
    if game_timer > 0:
        game_timer -= (clock.tick(60) / 1000)
    return game_timer