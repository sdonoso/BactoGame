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
from Player import *
from etapa1 import *

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
# se crea el jugador
player1 = Player("Red", [])

# se crean las colonias
colonias = crear_colonias(surface)
# se otorga una colonia al player
colonias[0].set_number(20)
player1.set_colonias(colonias[0])

# se crean las bacterias
bactum = Bacterium(0, 0, 0, 0, 0, bacteria, surface)

select_colony = []
posin = None
posfin = None
bact_llegada = None
bact_partida = None
dibujar = 0
selColony = None
initialT = 0

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
                selColony = find_colony(colonias, posin, player1)  # la colonia seleccionada con el mouse
                # if selColony != None:

                bact_partida = mouse_pos
                bactum.set_pos(bact_partida)
                posfin = mouse_pos
                select_colony.append(selColony)

            else:
                bact_llegada = mouse_pos
                #find_Ocolony(colonias,bact_llegada,player1)

                select_colony = []
                dibujar = 1
                bactum.move_to(bact_partida, bact_llegada)
                posin = None
                posfin = None

    initialT +=1
    # Dibuja la pantalla
    surface.fill(COLOR_WHITE)
    # Dibujo las colonias
    for colony in colonias:
        colony.draw()
    # se dibuja el numero de bacterias en las colonias
    dibuja_numero(colonias, surface)
    # cada tres segundos aumenta numero de colonias
    if initialT % 60 == 0 and initialT/60 ==3:
        initialT= 0
        for colony in colonias:
            if colony.get_color() !="Gray":
                colony.set_number(1)

    # se va dibujando la linea de seleccion
    if selColony != None:
        pos_fin = pygame.mouse.get_pos()
        pygame.draw.line(surface, COLOR_GRAY, posin, pos_fin, 3)
        selColony.draw_circ()

        # se dibujan las bacterias
        # if dibujar == 1:

        # bactum.move(colony2)
        # bactum.rot_center()
        # actualp = bactum.get_pos()
        # bactum.draw()
        # if abs(bact_llegada[0] - actualp[0]) < 10 and abs(bact_llegada[1] - actualp[1] < 10):
        # bactum.reset_move()
        # dibujar = 0
        # bact_llegada = None
        # bact_partida = None
        # bactum.set_pos([0, 0])

    pygame.display.flip()
