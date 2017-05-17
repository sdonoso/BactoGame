import pygame
import random
from Constantes import *
from funciones_extras import *


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
        self.numerollegada = 0
        self.tipo = None

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
        self.image_color()
        self.scale()
        self.surface.blit(self.image, (int(self.x), int(self.y)))

    def draw_circ(self):
        self.scale()
        return pygame.draw.circle(self.surface, COLOR_YELLOW, self.get_centro(), self.get_radio(), 3)

    def get_radio(self):
        return self.image.get_size()[1] / 2

    def get_centro(self):
        centro = [self.image.get_size()[0] / 2 + self.x, self.image.get_size()[1] / 2 + self.y]

        return centro

    def set_nllega(self, num, color):
        self.numerollegada = num
        self.otroc = color

    def llego(self, color, tipo):
        if self.color == "Gray" or self.color == color:
            self.set_number(1)
            self.color = color
            self.tipo = tipo
        else:
            if tipo == SPEED or tipo == REPRODUCTION:
                self.set_number(-1)
                self.revisar(tipo, color)
            elif tipo == DEFENCE:
                a = random.random()
                if a < 0.3:  # mas probabilidades de resistir ataques
                    self.set_number(-1)
                    self.revisar(tipo, color)

    def set_id(self, id):
        self.id = id

    def scale(self):
        if self.number <= 10:

            self.image = pygame.transform.scale(self.image, (50, 50))
        elif self.number < 20:
            self.image = pygame.transform.scale(self.image, (100, 100))
        elif self.number < 30:
            self.image = pygame.transform.scale(self.image, (130, 130))
        elif self.number < 40:
            print(self.number)
            self.image = pygame.transform.scale(self.image, (160, 160))
        elif self.number < 80:
            self.image = pygame.transform.scale(self.image, (180, 180))

    def image_color(self):
        if self.color == "Green":
            self.image = load_image('res/bacverde.png')
        elif self.color == "Rosa":
            self.image = load_image('res/bacrosa.png')

    def set_tipo(self, tipo):
        self.tipo = tipo

    def revisar(self, tipo, color):
        if self.number == 0:
            self.color = color
            self.tipo = tipo
