import pygame
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


def crear_bacterias(bacterias, colony, partida, llegada, surface,colony_llegada):
    player1 = load_image('res/bacteria.png')
    nbact = colony.get_number() / 2
    colony.set_number(-nbact)
    x = partida[0]
    y = partida[1]
    for i in range(nbact):
        a = Bacterium(x, y, 0, 0, 0, player1, surface, colony.id,colony_llegada,colony.tipo,colony.color)
        a.move_to([x,y],llegada)
        bacterias.append(a)
        #bacterias[i].move_to([x, y], llegada) #problema
        x += 6
        y -= 6
    return bacterias


def pause(surface):
    p=True
    font = pygame.font.Font(FONT, 100)
    text = font.render('PAUSA', 1, COLOR_BLACK)
    while p:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    p= False
                    break
        surface.blit(text, (SWIDTH / 2, SHEIGHT / 2))
        pygame.display.flip()
