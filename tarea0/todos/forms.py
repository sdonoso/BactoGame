from django import forms
from  todos.models import Todo

class ToDoForm(forms.Form):
    tarea = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder' : 'Nueva Tarea'}))