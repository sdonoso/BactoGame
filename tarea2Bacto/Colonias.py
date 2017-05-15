import pygame
import random
from Constantes import *


class Colony:
    def __init__(self, x, y, image, surface, color="Gray", number="0"):
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.number = int(number)
        self.image = image
        self.surface = surface
        self.rect = image.get_rect()
        self.rect.centerx = self.x + (image.get_size()[0] / 2)
        self.rect.centery = self.y + (image.get_size()[1] / 2)

    def set_color(self, newColor):
        """
        change colony color
        :param self:
        :param newColor:
        :return:
        """
        self.color = newColor
    def get_color(self):
        return self.color
    def set_number(self, newNumber):
        self.number += newNumber

    def get_number(self):
        return self.number

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPos(self):
        pos = []
        pos.append(self.x + 30)
        pos.append(self.y + 30)
        return pos

    def get_area(self):
        area = []
        area.append(self.x + self.image.get_size()[0])
        area.append(self.y + self.image.get_size()[1])
        return area

    def draw(self):
        self.surface.blit(self.image, (int(self.x), int(self.y)))

    def draw_circ(self):
        return pygame.draw.circle(self.surface, COLOR_YELLOW, self.get_centro(), self.get_radio(), 3)

    def get_radio(self):
        return self.image.get_size()[1] / 2

    def get_centro(self):
        centro = [self.image.get_size()[0] / 2 + self.x, self.image.get_size()[1] / 2 + self.y]

        return centro
