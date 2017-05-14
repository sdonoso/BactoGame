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

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_pos(self):
        return [self.x, self.y]

    def move_to(self, posIn, posFin):
        """
        mueve las bacterias a la colonia indicada con el mouse
        :param pos:
        :return:
        """

        self.dx = posFin[0] - posIn[0]
        self.dy = posFin[1] - posIn[1]
        self.stepX = self.dx / 100.
        self.stepY = self.dy / 100.

    def move(self):
        print("------------")
        self.x += self.stepX/2
        self.y += self.stepY/2

        # colision con techo


    def reset_move(self):
        self.stepY = 0
        self.stepX = 0
        self.dx = 0
        self.dy = 0

    def draw(self):
        self.surface.blit(self.image, (int(self.x), int(self.y)))
