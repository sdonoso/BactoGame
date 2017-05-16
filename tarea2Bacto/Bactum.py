# Imports

import os
from Player import *
from etapa1 import *
from enemigo import Enemy

# se inicia el modulo
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# se cargan los recursos
background1 = load_image('res/fondo.jpg')
background2 = load_image('res/fondo3.jpg')
pla= load_image('res/bacverde.png')
enemi = load_image(('res/bacrosa.png'))

bacteria = load_image('res/bacteria.png')

# se inicia la pantalla
surface = pygame.display.set_mode((SWIDTH, SHEIGHT))
pygame.display.set_caption('Bactum')

# se crea el reloj
clock = pygame.time.Clock()
# se crea el jugador
player1 = Player("Green", [],SPEED)
#se crea contrincante
enemy = Enemy("Rosa",REPRODUCTION)

# se crean las colonias
colonias = crear_colonias(surface)
# se otorga una colonia al player
colonias[3].set_number(20)
player1.set_colonias(colonias[3])
colonias[5].set_number(20)
enemy.set_colonia(colonias[5])

# se crean las bacterias
bacterias = []
bacterias_enemy =[]

pressButton = 0
posin = None
posfin = None
bact_llegada = None
bact_partida = None
selColony = None
initialT = 0
colonia_llegada = None

# Entra en el bucle principal
while True:
    # setea el reloj
    clock.tick(FPS)
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == QUIT:
            exit()
        # detecto pausa
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause(surface)
        # detecto el mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pressButton == 0:
                posin = mouse_pos
                selColony = find_colony(colonias, posin, player1)  # la colonia seleccionada con el mouse
                if selColony != None:
                    # if selColony != None:

                    bact_partida = mouse_pos
                    posfin = mouse_pos
                    pressButton = 1

            else:
                bact_llegada = mouse_pos
                opcion = find_arriveColony(colonias, bact_llegada, player1)
                if opcion == None:  # se ve si la posicion de llegada es valida
                    pressButton = 0
                    selColony = None
                else:
                    colonia_llegada = opcion
                    pressButton = 0
                    dibujar = 1
                    bacterias = crear_bacterias(bacterias, selColony, bact_partida, bact_llegada, surface, opcion)
                    posin = None
                    posfin = None
                    selColony = None

    initialT += 1  # Tiempo transcurrido
    # Dibuja la pantalla
    surface.fill(COLOR_WHITE)
    surface.blit(background2, (0, 0))
    # Dibujo las colonias
    # print("---"+str(len(bacterias)))

    for colony in colonias:
        colony.draw()
    # se dibuja el numero de bacterias en las colonias
    dibuja_numero(colonias, surface)
    # cada tres segundos aumenta numero de colonias
    if initialT % 60 == 0 and initialT / 60 == 3:
        enemy.atacar(colonias,bacterias_enemy,surface)
        initialT = 0
        for colony in colonias:
            if colony.get_color() != "Gray": #Falata poner que si es de tipo reproduccion se reprodusca faster
                colony.set_number(1)

    # se va dibujando la linea de seleccion
    if selColony != None:
        pos_fin = pygame.mouse.get_pos()
        pygame.draw.line(surface, COLOR_GRAY, posin, pos_fin, 3)
        selColony.draw_circ()
    #---------------------------------------------------------------------------
    # se dibujan las bacterias
    for bact in bacterias[:]:
        if bact.llegada != 'si':
            invalid = bact.move(colonias)
            # bactum.rot_center()
            # actualp = bactum.get_pos()
            bact.draw()

    for bac in bacterias[:]:  # remuevo del arreglo las bacterias que llegaron
        if bac.llegada == 'si':
            bacterias.remove(bac)
    # ---------------------------------------------------------------------------
    #se dibujan las bacterias enemigas
    for bac in bacterias_enemy[:]:
        if bac.llegada !='si':
            Einvalid = bac.move(colonias)
            bac.draw()
    #remuevo las que llegaron
    for bac in bacterias_enemy[:]:
        if bac.llegada == 'si':
            bacterias_enemy.remove(bac)
    # ---------------------------------------------------------------------------
    pygame.display.flip()
