from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('', views.listadoPosts, name='inicio'),
    path(' post/<pk>', views.detalles, name='detalles'),
    path('post/nuevo/', views.nuevoPost, name='nuevoPost'),
    path('post/<pk>/modificar', views.modificar, name='modificar'),
]
