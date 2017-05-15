from Constantes import *
import math
import pygame


class Bacterium:
    def __init__(self, x, y, speed, rTime, defense, image, surface):
        self.speed = speed
        self.rTime = rTime
        self.defense = defense
        self.x = x
        self.y = y
        self.image = image
        self.surface = surface
        self.stepX = 0
        self.stepY = 0
        self.dx = 0
        self.dy = 0
        self.posF = 0
        self.angulo = 0
        self.l = 0

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_pos(self):
        return [self.x, self.y]

    def move_to(self, posIn, posFin):
        """
        establece cuanto necesita moverse
        :param pos:
        :return:
        """
        self.posF = posFin
        self.dx = posFin[0] - posIn[0]
        self.dy = posFin[1] - posIn[1]
        self.stepX = self.dx / 100.
        self.stepY = self.dy / 100.

    def move(self, colony):
        """
        muevele la particula
        :return:
        """
        # if self.l == 0:
        # self.impact(colony)
        # if self.angulo == 0:
        if not self.impact(colony):
            self.x += self.stepX / 2
            self.y += self.stepY / 2
            # self.y = self.kls+50*math.sin(2*math.pi*0.01*self.x)
            # else:
            # self.move_on_rx(colony)

    def impact(self, colony):
        """
        evita impacto con colonias no seleccionadas
        :param colony:
        :return:
        """
        if abs(self.y - colony.y) <= 10 and colony.x + 5 <= self.x <= colony.get_area()[0]:
            # self.r = math.sqrt((colony.get_centro()[0] - self.x) ** 2 + (colony.get_centro()[1] - self.y) ** 2)

            # self.l =1
            self.move_on_x()
            print(1)
            return True
        elif abs(self.x - colony.x) <= 10 and colony.y <= self.y <= colony.get_area()[1]:
            # self.r = math.sqrt((colony.get_centro()[0] - self.x) ** 2 + (colony.get_centro()[1] - self.y) ** 2)

            # self.l = 1
            self.move_on_y()
            print (2)
            return True
        elif abs(self.y - colony.get_area()[1]) <= 10 and colony.x + 5 <= self.x <= colony.get_area()[0]:
            #self.r = math.sqrt((colony.get_centro()[0] - self.x) ** 2 + (colony.get_centro()[1] - self.y) ** 2)

            #self.l = 1
            self.move_on_x()
            print(3)
            return True
        elif abs(self.x - colony.get_area()[0]) <= 10 and colony.y <= self.y <= colony.get_area()[1]:
            #self.r = math.sqrt((colony.get_centro()[0] - self.x) ** 2 + (colony.get_centro()[1] - self.y) ** 2)

            #self.l = 1
            self.move_on_y()
            print(4)
            return True
        return False

    def move_on_x(self):
        if self.x > self.y:
            self.x += 1
        else:
            self.x -= 1
        pinicial = [self.x, self.y]
        self.move_to(pinicial, self.posF)

    def move_on_y(self):
        self.y += 1
        pinicial = [self.x, self.y]
        self.move_to(pinicial, self.posF)

    def move_on_rx(self, colony):
        self.x = self.r * math.cos(self.angulo) + colony.get_centro()[0]
        self.y = self.r * math.sin(self.angulo) + colony.get_centro()[1]
        self.angulo += 0.05
        if self.angulo >= 2 * math.pi:
            self.angulo = 0
            self.l = 0
        pinicial = [self.x, self.y]
        self.move_to(pinicial, self.posF)

    def reset_move(self):
        self.stepY = 0
        self.stepX = 0
        self.dx = 0
        self.dy = 0

    def draw(self):
        self.surface.blit(self.image, (int(self.x), int(self.y)))

    def rot_center(self):
        self.image = pygame.transform.rotate(self.image, 90)

    def scale(self):
        self.image = pygame.transform.scale(self.image, (60, 60))
