from Colonias import *
from funciones_extras import *

cimagen = load_image('res/bacneu.png')


def crear_colonias(surface):
    #para tener mas etapas agrego un parametro que pida etapa
    colonias = [Colony(50, 50, cimagen, surface), Colony(200, 200, cimagen, surface),
                Colony(650, 650, cimagen, surface), Colony(200, 50, cimagen, surface),
                Colony(50, 500, cimagen, surface), Colony(400, 400, cimagen, surface),
                Colony(400, 600, cimagen, surface)]
    ids=range(len(colonias))
    i=0
    for col in colonias:
        col.set_id(ids[i])
        i+=1
    return colonias
