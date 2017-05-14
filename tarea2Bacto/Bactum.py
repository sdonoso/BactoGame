# Imports
from Constantes import *
from pygame.locals import *
import os
import math
import pygame
from Colonias import Colony
from funciones_extras import *
from Bacteria import Bacterium
import random

# se inicia el modulo
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# se cargan los recursos
colonia = load_image('res/bactichica.png')
colonia2 = load_image('res/bacti.png')
bacteria = load_image('res/bacteria.png')

# se inicia la pantalla
surface = pygame.display.set_mode((SWIDTH, SHEIGHT))
pygame.display.set_caption('Bactum')

# se crea el reloj
clock = pygame.time.Clock()
# Colonias
colonys = []

# se crean las colonias
colony = Colony(50, 50, colonia, surface)
colony2 = Colony(400, 400, colonia2, surface)
print (colony2.image.get_size())
print (colony.rect)
# se crean las bacterias
bactum = Bacterium(0, 0, 0, 0, 0, bacteria, surface)

select_colony = []
colonys = [colony, colony2]
posin = None
posfin = None
bact_llegada = None
bact_partida = None
dibujar = 0

# Entra en el bucle principal
while True:
    # setea el reloj
    clock.tick(FPS)
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == QUIT:
            exit()
        # detecto el mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if select_colony == []:
                posin = mouse_pos
                bact_partida = mouse_pos
                bactum.set_pos(bact_partida)
                posfin = mouse_pos
                select_colony.append(1)

            else:
                print("waaa")

                select_colony = []
                dibujar = 1
                bact_llegada = mouse_pos
                bactum.move_to(bact_partida, bact_llegada)
                posin = None
                posfin = None

    mouse = pygame.mouse.get_pressed()

    # Dibuja la pantalla
    surface.fill(COLOR_WHITE)
    # Dibujo las colonias
    colony2.draw()
    colony.draw()
    # se dibuja el numero de bacterias en las colonias
    dibuja_numero(colonys, surface)

    # se va dibujando la linea de seleccion
    if posin != None:
        pos_fin = pygame.mouse.get_pos()
        pygame.draw.line(surface, COLOR_GRAY, posin, pos_fin, 3)

    # se dibujan las bacterias
    if dibujar == 1:

        bactum.move()
        actualp = bactum.get_pos()
        bactum.draw()
        if abs(bact_llegada[0] - actualp[0]) < 10 and abs(bact_llegada[1] - actualp[1] < 10):
            bactum.reset_move()
            dibujar = 0
            bact_llegada = None
            bact_partida = None
            bactum.set_pos([0, 0])

    pygame.display.flip()
