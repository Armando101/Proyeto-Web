from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.listadoPosts, name='inicio' ),
    path(' post/<pk>', views.detalles, name='detalles'),
    path('post/nuevo/', views.nuevoPost, name='nuevoPost'),
    path('post/<pk>/modificar', views.modificar, name='modificar'),
]
