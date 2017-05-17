from random import choice
from funciones_extras import *


class Enemy:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

    def atacar(self, colonias, bacterias, surface):
        c_partida = None
        for colonia in colonias:  # se elige colonia propia
            if colonia.color == self.color:
                c_partida = colonia
                break
        i = 0
        indices = []
        for colonia in colonias:  # veo colonias que puedo atacar
            if colonia.color != self.color:
                indices.append(i)
            i += 1

        n = choice(indices)  # se elige colonia que se atacara
        partida = c_partida.get_centro()
        c_llegada = colonias[n]
        p_llegada = c_llegada.get_centro()
        return crear_bacterias(bacterias, c_partida, partida, p_llegada, surface, c_llegada)

    def set_colonia(self, colonia):
        colonia.set_color(self.color)
        colonia.set_tipo(self.tipo)
        colonia.set_number(20)

    def atacar_I(self, colonias, bacterias, surface, attack):
        if attack.color !=self.color:
            c_partida = None
            for colonia in colonias:  # se elige colonia propia
                if colonia.color == self.color:
                    c_partida = colonia
                    break

            partida = c_partida.get_centro()
            c_llegada = attack
            p_llegada = c_llegada.get_centro()
            return crear_bacterias(bacterias, c_partida, partida, p_llegada, surface, c_llegada)
