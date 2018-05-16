from .models import Todo


def sort(objetos, a):
    b=[]
    for obj in objetos:
        b.insert(obj.posicion, obj)
    for i in b:
        a.insert(0,i)
    return a


def changepos(pos):
    tareas = Todo.objects.all()
    for objeto in tareas:
        if (objeto.posicion > pos):
            pnew = objeto.posicion
            objeto.posicion = pnew - 1
            objeto.save()


def move(place, pos):
    length=len(Todo.objects.all())-1
    if(place== "down" and pos ==0 or place == "up" and pos==length):
        return

    elif (place == "up"):
        tUp = Todo.objects.get(posicion=pos)
        tDown = Todo.objects.get(posicion=pos + 1)
        tUp.posicion = tDown.posicion
        tUp.save()
        tDown.posicion = pos
        tDown.save()
    elif (place == "down"):
        tDown = Todo.objects.get(posicion=pos)
        tUp = Todo.objects.get(posicion=pos - 1)
        tUp.posicion = tDown.posicion
        tUp.save()
        tDown.posicion = pos-1
        tDown.save()
