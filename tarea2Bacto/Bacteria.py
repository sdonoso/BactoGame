from Constantes import *


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

    def move(self):
        """
        muevele la particula
        :return:
        """
        self.x += self.stepX / 2
        self.y += self.stepY / 2

    def impact(self, colony):
        """
        evita impacto con colonias no seleccionadas
        :param colony:
        :return:
        """
        size = []
        size.append(colony.image.get_size()[0] * 0.5)
        size.append(colony.image.get_size()[1] * 0.5)

        if abs(self.x + 20 - colony.get_area()[0]) < size[0] and abs(self.y + 20 - colony.get_area()[1]) < size[1]:
            # si estoy mas serca por x
            if abs(self.x + 20 - colony.get_area()[0]) > abs(self.y + 20 - colony.get_area()[1]):
                self.move_on_y(size)
            else:
                self.move_on_x(size)
        elif abs(self.x + 20 - colony.getX()) < size[0] and abs(self.y + 20 - colony.getY()) < size[1]:
            if abs(self.x + 20 - colony.getX()) > abs(self.y + 20 - colony.getY()):
                self.move_on_y(size)
            else:
                self.move_on_x(size)

    def move_on_x(self, size):
        self.x += size[0]
        pinicial = [self.x, self.y]
        self.move_to(pinicial, self.posF)

    def move_on_y(self, size):
        self.y += size[0]
        pinicial = [self.x, self.y]
        self.move_to(pinicial, self.posF)

    def reset_move(self):
        self.stepY = 0
        self.stepX = 0
        self.dx = 0
        self.dy = 0

    def draw(self):
        self.surface.blit(self.image, (int(self.x), int(self.y)))
