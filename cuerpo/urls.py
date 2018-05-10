from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
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
