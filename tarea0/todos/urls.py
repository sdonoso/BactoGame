from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^agregar', views.agregar, name='agregar'),
    url(r'^delet', views.delet, name='delet'),
    url(r'^up', views.up, name='up'),
    url(r'^down', views.down, name='down'),

]
