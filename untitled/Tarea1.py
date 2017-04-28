# coding=utf-8



import numpy as np
import matplotlib.pyplot as plt
import random
import math
import tqdm
import ecuaciones

# Constantes
ALPHA = 1
ITERATIONS = 100


class Perfil(object):
    def __init__(self, widht, high, hora):
        """
        Constructor

        :param ancho: ancho del perfin el Km
        :param alto: alto del perfil en Km
        """
        self.width = widht
        self.high = high
        self.hora = hora

        h = 0.01  # hace el perfil de 400 X 800

        self.highP = int(widht / h)
        self.widhtP = int(high / h)


        # se crea la matriz
        self.matrix = np.zeros((self.highP, self.widhtP))

    def __str__(self):
        """
        Imprime la matriz
        :return:
        """
        print self.matrix
        return ''

    def suelo_mar(self):
        """
        se calcula la parte de tierra  y mar aleatoriamente con restriccion
        del mar
        :return:
        """
        self.sea = int(self.widhtP * (round(random.uniform(30, 40)) / 100))
        self.land = int(self.widhtP - self.sea)
        temperaturaMar = ecuaciones.temperatura_mar(self.hora)

        for j in range(1, 20):
            nivel = j

            for i in range(0, self.sea + 1):
                self.matrix[len(self.matrix) - nivel, i] = temperaturaMar

    def crear_montanhas(self):
        """
        Crea las montanhas
        :param self:
        :return: nada
        """
        p = self.sea

        for i in range(10):
            partida = len(self.matrix)
            alturaMontanha = int(random.uniform(0, self.highP * ALPHA))
            numeroCapas = alturaMontanha / 10
            anchoCapa = int(random.uniform(alturaMontanha, 2 * alturaMontanha))
            anchoInicial = anchoCapa

            for capas in range(numeroCapas):
                s = p + (anchoInicial / 2)
                for j in range(1, 10):  # cantidad de celdas para el mar

                    for k in range(anchoCapa / 2):
                        if s + k < self.widhtP:
                            self.matrix[partida - j, s + k] = 15
                            self.matrix[partida - j, s - k] = 15

                anchoCapa = int(random.uniform(anchoCapa * 0.5, anchoCapa))
                partida = partida - 9
            p = p + (anchoInicial / 4)

    def crear_chimenea(self):
        temperatura = 500 * (math.cos(self.hora * math.pi / 12) + 2)
        posicion = self.sea
        p2 = 20
        for j in range(10):
            for i in range(5):  # 100 metros de chimenea para esta discretizacion igual a 5 celdas
                self.matrix[len(self.matrix) - p2, posicion - i] = temperatura
            p2 += 1

    def temp_atmosfera(self):
        temperaturaAtmosfera = ecuaciones.temperatura_mar(self.hora)
        for i in range(self.widhtP):
            for j in range(self.highP):
                if j <= 179:
                    self.matrix[j, i] = temperaturaAtmosfera - 6
                else:
                    self.matrix[j, i] = temperaturaAtmosfera

    def iterate(self):
        for _ in tqdm.tqdm(range(ITERATIONS)):

            for i in range(1, self.highP - 21):  # filas
                for j in range(1, self.widhtP - 1):  # columnas
                    if self.matrix[i, j] != 15:
                        if self.matrix[i + 1, j] == 15 and self.matrix[i, j + 1] == 15:
                            self.matrix[i, j] = 0.5 * (self.matrix[i - 1, j] + self.matrix[i, j - 1])
                        elif self.matrix[i + 1, j] == 15 and self.matrix[i, j - 1] == 15:
                            self.matrix[i, j] = 0.5 * (self.matrix[i - 1, j] + self.matrix[i, j + 1])
                        elif self.matrix[i + 1, j] == 15:
                            self.matrix[i, j] = 0.25 * (
                                2 * self.matrix[i - 1, j] + self.matrix[i, j - 1] + self.matrix[i, j + 1])
                        elif self.matrix[i, j - 1] == 15:
                            self.matrix[i, j] = 0.25 * (
                                2 * self.matrix[i, j + 1] + self.matrix[i + 1, j] + self.matrix[i - 1, j])
                        elif self.matrix[i, j + 1] == 15:
                            self.matrix[i, j] = 0.25 * (
                                2 * self.matrix[i, j - 1] + self.matrix[i + 1, j] + self.matrix[i - 1, j])
                        else:
                            self.matrix[i, j] = 0.25 * (
                                self.matrix[i, j + 1] + self.matrix[i, j - 1] + self.matrix[i + 1, j] + self.matrix[
                                    i - 1, j])

    def plot(self):
        """
        Plotea la solución
        :return:
        """

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Se agrega grafico al plot
        cax = ax.imshow(self.matrix)
        fig.colorbar(cax)

        plt.show()


if __name__ == '__main__':
    est = Perfil(2, 4,8)
    est.temp_atmosfera()
    est.suelo_mar()
    est.crear_montanhas()
    #est.crear_chimenea()
    #est.iterate()

    print est
    est.plot()
