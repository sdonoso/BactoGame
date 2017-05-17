from random import randint, choice
import time
import pygame
import Colonias
from Constantes import *
from Bacteria import Bacterium
from pygame.locals import *


def load_image(image):
    """
    Carga la imagen
    :param image:
    :return:
    """
    return pygame.image.load(image)


cimagen = load_image('res/bacneu.png')


def crear_colonias(surface):
    # se fija posicion en X y se eleije al azar en Y para que no se topen
    colonias = [Colonias.Colony(30, randint(10, 300), cimagen, surface),
                Colonias.Colony(200, randint(10, 500), cimagen, surface),
                Colonias.Colony(500, randint(10, 700), cimagen, surface),
                Colonias.Colony(400, randint(300, 600), cimagen, surface),
                Colonias.Colony(850, randint(100, 700), cimagen, surface),
                Colonias.Colony(125, randint(400, 700), cimagen, surface),
                Colonias.Colony(700, randint(100, 700), cimagen, surface)]
    ids = range(len(colonias))
    i = 0
    for col in colonias:
        col.set_id(ids[i])
        i += 1
    return colonias


def dibuja_numero(colonys, surface):
    """
    Dibuja el numero de bacterias en las colonias
    :param colonys: colonias
    :param surface: surface del juego
    :return:
    """
    font = pygame.font.Font(FONT, 40)
    for colony in colonys:
        number = str(colony.get_number())
        center = colony.get_centro()
        center[1] = center[1] - 15
        center[0] = center[0] - 10
        render = font.render(number, 1, COLOR_ORANGE)
        surface.blit(render, center)


def find_colony(colonys, pos, player):
    """
    busca la colonia en la posicion que se hizo click
    :param colonys:
    :return:
    """

    for colony in colonys:
        area = colony.get_area()
        if colony.x <= pos[0] <= area[0] and colony.y < pos[1] < area[1]:
            if colony.get_color() == player.get_color():
                return colony
    return None


def find_arriveColony(colonys, pos, player):
    """
    busca si la posicion de llegada es valida
    :param colonys:
    :param pos:
    :param player:
    :return:
    """
    for colony in colonys:
        area = colony.get_area()
        if colony.x <= pos[0] <= area[0] and colony.y < pos[1] < area[1]:
            if colony.get_color() != player.get_color():
                return colony
    return None


def crear_bacterias(bacterias, colony, partida, llegada, surface, colony_llegada):
    player1 = load_image('res/bacteria.png')
    nbact = colony.get_number() / 2
    colony.set_number(-nbact)
    x = partida[0]
    y = partida[1]
    for i in range(nbact):
        a = Bacterium(x, y, player1, surface, colony.id, colony_llegada, colony.tipo, colony.color)
        a.move_to([x, y], llegada)
        bacterias.append(a)
        # bacterias[i].move_to([x, y], llegada) #problema
        x += 6
        y -= 6
    return bacterias


def pause(surface):
    p = True
    font = pygame.font.Font(FONT, 100)
    text = font.render('PAUSA', 1, COLOR_BLACK)
    while p:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    p = False
                    break
        surface.blit(text, (SWIDTH / 2, SHEIGHT / 2))
        pygame.display.flip()


def menu(surface, player1, enemy):
    colonias = crear_colonias(surface)  # se inicia la etapa
    p = True
    surface.fill(COLOR_BLACK)
    font = pygame.font.Font(FONT, 40)
    font2 = pygame.font.Font(FONT, 30)
    titulo = font.render('ELIGE LA HABILIDAD DE TU BACTERIA', 1, COLOR_WHITE)
    titulo2 = font.render('TU COLOR ES EL VERDE', 1, COLOR_WHITE)
    speed = font2.render('VELOCIDAD', 1, COLOR_WHITE)
    defenced = font2.render('DEFENSA', 1, COLOR_WHITE)
    repro = font2.render('REPRODUCCION', 1, COLOR_WHITE)
    rect1 = pygame.draw.rect(surface, COLOR_GRAY, [100, 400, 250, 100], 0)
    rect2 = pygame.draw.rect(surface, COLOR_GRAY, [400, 400, 250, 100], 0)
    rect3 = pygame.draw.rect(surface, COLOR_GRAY, [700, 400, 250, 100], 0)
    pos1 = [100, 400, 350, 500]
    pos2 = [400, 400, 650, 500]
    pos3 = [700, 400, 950, 500]

    while p:
        surface.fill(COLOR_BLACK)
        rect1 = pygame.draw.rect(surface, COLOR_GRAY, [100, 400, 250, 100], 0)
        rect2 = pygame.draw.rect(surface, COLOR_GRAY, [400, 400, 250, 100], 0)
        rect3 = pygame.draw.rect(surface, COLOR_GRAY, [700, 400, 250, 100], 0)
        p_mouse = pygame.mouse.get_pos()
        if pos1[0] <= p_mouse[0] <= pos1[2] and pos1[1] <= p_mouse[1] <= pos1[3]:
            pygame.draw.rect(surface, COLOR_YELLOW, [100, 400, 250, 100], 3)
        elif pos2[0] <= p_mouse[0] <= pos2[2] and pos2[1] <= p_mouse[1] <= pos2[3]:
            pygame.draw.rect(surface, COLOR_YELLOW, [400, 400, 250, 100], 3)
        elif pos3[0] <= p_mouse[0] <= pos3[2] and pos3[1] <= p_mouse[1] <= pos3[3]:
            pygame.draw.rect(surface, COLOR_YELLOW, [700, 400, 250, 100], 3)

        surface.blit(titulo, (100, 10))
        surface.blit(titulo2, (300, 300))
        surface.blit(speed, (130, 430))
        surface.blit(defenced, (450, 430))
        surface.blit(repro, (730, 430))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos1[0] <= p_mouse[0] <= pos1[2] and pos1[1] <= p_mouse[1] <= pos1[3]:
                    p = False
                    player1.tipo = SPEED  # seteo el tipo que se eligio
                    enemy.tipo = choice([DEFENCE, REPRODUCTION])
                    player1.set_colonias(colonias[1])
                    enemy.set_colonia(colonias[2])
                    return SPEED, colonias
                elif pos2[0] <= p_mouse[0] <= pos2[2] and pos2[1] <= p_mouse[1] <= pos2[3]:
                    p = False
                    player1.tipo = DEFENCE
                    enemy.tipo = choice([SPEED, REPRODUCTION])
                    player1.set_colonias(colonias[1])
                    enemy.set_colonia(colonias[2])
                    return DEFENCE, colonias
                elif pos3[0] <= p_mouse[0] <= pos3[2] and pos3[1] <= p_mouse[1] <= pos3[3]:
                    p = False
                    player1.tipo = REPRODUCTION
                    enemy.tipo = choice([DEFENCE, SPEED])
                    player1.set_colonias(colonias[1])
                    enemy.set_colonia(colonias[2])
                    return REPRODUCTION, colonias

        pygame.display.flip()


def clock_draw(tiempo, surface):
    font2 = pygame.font.Font(FONT, 30)
    hora = font2.render(time.strftime("%H:%M:%S", time.gmtime(tiempo)), 1, COLOR_BLACK)
    surface.blit(hora, (850, 10))


def perdiste(surface):
    p = True
    font = pygame.font.Font(FONT, 50)
    perder = font.render('PERDISTE', 1, COLOR_WHITE)
    reiniciar = font.render('REINICIA PRESIONANDO R', 1, COLOR_WHITE)

    while p:
        surface.fill(COLOR_BLACK)
        surface.blit(perder, (300, 300))
        surface.blit(reiniciar,(100,500))

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                p = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    p=False
                    break

        pygame.display.flip()

def ganas(surface):
    colonias = crear_colonias(surface)  # se inicia la etapa
    p = True
    font = pygame.font.Font(FONT, 50)
    ganar = font.render('GANASTE', 1, COLOR_WHITE)
    reiniciar = font.render('REINICIA PRESIONANDO R', 1, COLOR_WHITE)
    while p:
        surface.fill(COLOR_BLACK)
        surface.blit(ganar, (300, 300))
        surface.blit(reiniciar,(100,500))
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                p = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    p=False
                    break
        pygame.display.flip()

