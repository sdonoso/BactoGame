from PIL import Image


class Colony:
    def __init__(self, x, y, image, surface, color="COLOR_GRAY", number="0"):
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
