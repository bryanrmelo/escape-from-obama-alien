import pygame
import time
r = 255
g = 255
b = 255
x = 18623123
branco_ciano = False
ciano_azul = False
azul_rosa = False
rosa_vermelho = False
vermelho_amarelo = False
amarelo_verde = False
ultima_rep = False
rep = True
while rep:
    for i in range(x):
        if r <= 255 and g == 255 and b == 255:
            r -= 1
            if r == 0:
                branco_ciano = True
                amarelo_verde = False
            #branco para azul ciano
        if r == 0 and g <= 255 and b == 255 and branco_ciano == True:
            g -= 1
            if g == 0:
                ciano_azul = True
                branco_ciano = False
            # azul ciano para azul
        if r >= 0 and g == 0 and b == 255 and ciano_azul == True:
            if r != 255:
                r += 1
                if r == 255 and b == 255:
                    azul_rosa = True
                    ciano_azul = False
            # azul para rosa
        if r <= 255 and g == 0 and b <= 255 and azul_rosa == True:
            b -= 1
            if b == 0:
                rosa_vermelho = True
                azul_rosa = False
            # rosa para vermelho
        if r <= 255 and g >= 0 and b >= 0 and rosa_vermelho == True:
            if g != 255:
                g += 1
                if r == 255 and g == 255:
                    vermelho_amarelo = True
                    rosa_vermelho = False

            # vermelho para amarelo
        if r <= 255 and g == 255 and b == 0 or b == 1 and vermelho_amarelo == True:
            r -= 1
            if r == 0:
                amarelo_verde = True
                rosa_vermelho = False
            # amarelo para verde
        if r >= 0 and g == 255 and b >= 0 and amarelo_verde == True:
            if r != 255 and b != 255:
                r += 1
                b += 1
        time.sleep(0.001)
