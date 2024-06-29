from django.urls import path
from . import views

urlpatterns = [
    path('main/index.html', views.mostrar_index, name='index'),
    path('main/registrarse.html/', views.mostrar_regis, name='registrarse'),
    path('main/carrito.html/', views.mostrar_carrito, name = 'carro'),
    path('herramientas.html/', views.mostrar_herramientas, name='herramientas'),
    path('jardineria.html/', views.mostrar_jardineria, name='jardineria'),
    path('nostros.html/', views.mostrar_nosotros, name='nosotros'),
    path('sesion.html/', views.mostrar_sesion, name='sesion'),
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/create/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:pk>/edit/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:pk>/delete/', views.usuario_delete, name='usuario_delete'),
    path('carrito/', views.carrito_list, name='carrito_list'),
    path('carrito/crear/', views.carrito_create, name='carrito_create'),
    path('carrito/editar/<int:pk>/', views.carrito_update, name='carrito_update'),
    path('carrito/eliminar/<int:pk>/', views.carrito_delete, name='carrito_delete'),
    
    
]