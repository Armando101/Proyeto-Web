from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('menuproductos/', views.menuproductos, name='menuproductos'),
    path('menuproductos/barnices/', views.barnices, name='barnices'),
    path('menuproductos/cabello/', views.cabello, name='cabello'),
    path('menuproductos/cuidado/', views.cuidado, name='cuidado'),
    path('menuproductos/perfumes/', views.perfumes, name='perfumes'),
    path('menuproductos/maquillaje/', views.maquillaje, name='maquillaje'),
    path('opiniones/', views.opiniones, name='opiniones'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('citas/', views.citas, name='citas'),
    path('login/cerrar', views.cerrar, name='cerrar'),
    path('registro/', views.registro, name='registro'),
    path('citas/', views.citas, name='citas'),
    path('tips/', views.tips, name='tips'),
    path('', views.listadoPosts, name='inicio'),
    path(' post/<pk>', views.detalles, name='detalles'),
    path('post/nuevo/', views.nuevoPost, name='nuevoPost'),
    path('post/<pk>/modificar', views.modificar, name='modificar'),
]
