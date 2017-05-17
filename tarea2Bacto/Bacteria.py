from Constantes import *
import math
import pygame


class Bacterium:
    def __init__(self, x, y, image, surface, id, cllega, tipo, color):
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
        self.moverse = 0
        self.id = id
        self.llegada = 'no'
        self.col_llega = cllega
        self.tipo = tipo
        self.color = color

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
        self.x = posIn[0]
        self.y = posIn[1]
        self.posF = posFin
        self.dx = posFin[0] - posIn[0]
        self.dy = posFin[1] - posIn[1]
        self.stepX = self.dx / 100.
        self.stepY = self.dy / 100.

    def move(self, colonys):
        """
        muevele la particula
        :return:
        """
        # if self.l == 0:
        # self.impact(colony)
        # if self.angulo == 0:
        for colony in colonys:  # se ve si se llego a la colonia seleccionada
            respuesta = self.llego(colony)
            if respuesta[0] == True:
                if respuesta[1] == 1:
                    # self.reset_move()
                    return 1
                else:
                    if self.tipo == SPEED: # si es de tipo velocidad se aumenta
                        self.x += self.stepX / 2 + 0.5
                        self.y += self.stepY / 2 + 0.5
                    else:
                        self.x += self.stepX / 2 + 0.5
                        self.y += self.stepY / 2 + 0.5
                    return 0


            elif not self.impact(colonys):
                self.x += self.stepX / 2
                self.y += self.stepY / 2
                # self.y = self.kls+50*math.sin(2*math.pi*0.01*self.x)

                return 0
            return 0

    def impact(self, colonys):
        """
        evita impacto con colonias no seleccionadas
        :param colony:
        :return:
        """

        for colony in colonys:
            if colony.id != self.id:
                if abs(self.y - colony.y) <= 10 and colony.x + 5 <= self.x <= colony.get_area()[0]:

                    self.move_on_x()
                    print(1)
                    return True
                elif abs(self.x - colony.x) <= 10 and colony.y <= self.y <= colony.get_area()[1]:

                    self.move_on_y()
                    print (2)
                    return True
                elif abs(self.y - colony.get_area()[1]) <= 10 and colony.x + 5 <= self.x <= colony.get_area()[0]:

                    self.move_on_x()
                    print(3)
                    return True
                elif abs(self.x - colony.get_area()[0]) <= 10 and colony.y <= self.y <= colony.get_area()[1]:

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

    def reset_move(self):
        self.stepY = 0
        self.stepX = 0
        self.dx = 0
        self.dy = 0

    def draw(self):
        if self.tipo == SPEED:
            self.rot_center()
        if self.llegada != 'si' and self.salirse_pantalla() == False:
            self.surface.blit(self.image, (int(self.x), int(self.y)))

    def rot_center(self):
        self.image = pygame.transform.rotate(self.image, -90)

    def scale(self):
        self.image = pygame.transform.scale(self.image, (60, 60))

    def llego(self, colony):
        if abs(self.y - self.col_llega.y) <= 10 and self.col_llega.x + 5 <= self.x <= self.col_llega.get_area()[
            0] or abs(
                    self.x - self.col_llega.x) <= 10 and self.col_llega.y <= self.y <= self.col_llega.get_area()[
            1] or abs(
                    self.y - self.col_llega.get_area()[1]) <= 10 and self.col_llega.x + 5 <= self.x <= \
                self.col_llega.get_area()[
                    0] or abs(
                    self.x - self.col_llega.get_area()[0]) <= 10 and self.col_llega.y <= self.y <= \
                self.col_llega.get_area()[1]:

            area = self.col_llega.get_area()
            if self.col_llega.x <= self.x <= area[0] and self.col_llega.y < self.y < area[1]:
                self.llegada = 'si'
                self.col_llega.llego(self.color, self.tipo)  # aviso a la colonia que llegue

                return [True, 1]
            else:
                return [True, 0]

        else:
            return [False, 0]

    def salirse_pantalla(self):
        if self.x < 0 or self.y < 0 or self.x > SWIDTH or self.y > SHEIGHT:
            return True
        else:
            return False
