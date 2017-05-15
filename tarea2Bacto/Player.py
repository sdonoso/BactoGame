class Player:
    def __init__(self, color, colonias):
        self.color = color
        self.colonias = colonias

    def get_color(self):
        return self.color

    def get_colonias(self):
        return self.colonias
    def set_colonias(self, colonia):
        colonia.set_color( self.color)
        #aca va coloni.load_image imagen del color
        self.colonias.append(colonia)
