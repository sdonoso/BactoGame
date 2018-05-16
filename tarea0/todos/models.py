# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models


class Todo(models.Model):
    tarea = models.TextField()
    posicion = models.IntegerField(default=-1 )
    def __str__(self):
        return self.tarea #muestra esto en la vista de la consola para el objeto
