from Colonias import *
from funciones_extras import *

cimagen = load_image('res/bactichica.png')


def crear_colonias(surface):
    #para tener mas etapas agrego un parametro que pida etapa
    colonias = [Colony(50, 50, cimagen, surface), Colony(200, 200, cimagen, surface),
                Colony(750, 750, cimagen, surface), Colony(200, 50, cimagen, surface),
                Colony(50, 700, cimagen, surface), Colony(400, 400, cimagen, surface),
                Colony(400, 700, cimagen, surface)]
    return colonias
