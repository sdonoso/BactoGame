from django.shortcuts import render, redirect

from .models import Todo
from todos.util import *


def index(request):
    a = []
    todos = Todo.objects.all()

    if (len(todos) > 0):
        todos = sort(todos, a)

    context = {
        'tareas': todos
    }
    return render(request, 'index.html', context)


def agregar(request):
    tarea = request.POST['tarea']
    all = Todo.objects.all()
    pos = len(all)

    todo = Todo(tarea=tarea, posicion=pos)
    todo.save()

    return redirect('/todos')


def up(request):
    id = request.POST['id']
    tarea = Todo.objects.get(id=id)
    move("up", tarea.posicion)
    return redirect('/todos')

def down(request):
    id = request.POST['id']
    tarea = Todo.objects.get(id=id)
    move("down", tarea.posicion)
    return redirect('/todos')


def delet(request):
    id = request.POST['id']
    tarea = Todo.objects.get(id=id)
    pos = tarea.posicion
    tarea.delete()
    changepos(pos)

    return redirect('/todos')
