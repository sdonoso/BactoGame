import pygame
from Constantes import *
from Colonias import Colony


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
        center = colony.getPos()
        render = font.render(number, 1, COLOR_ORANGE)
        surface.blit(render, center)


def find_colony(colonys, pos):
    """
    busca la colonia en la posicion que se hizo click
    :param colonys:
    :return:
    """
    for colony in colonys:
        area = colony.get_area
        if colony.getX() < pos[0] < area[0] and colony.getX() < pos[1] < area[1]:
            return colony
