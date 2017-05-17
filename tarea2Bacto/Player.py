class Player:
    def __init__(self, color, colonias, tipo):
        self.color = color
        self.colonias = colonias
        self.tipo = tipo

    def get_color(self):
        return self.color

    def get_colonias(self):
        return self.colonias
    def set_colonias(self, colonia):
        colonia.set_color( self.color)
        colonia.set_tipo(self.tipo)
        colonia.set_number(20)
        #aca va coloni.load_image imagen del color
        self.colonias.append(colonia)
