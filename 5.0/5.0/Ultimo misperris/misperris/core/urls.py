"""

from django.urls import path
from django.contrib import admin
from .views import menu,home,galeria,formulario,agregar_mascota,listar_mascotas,eliminar_mascotas,modificar_mascota
from core import views

urlpatterns = [
    path('', views.home,name='home'),
    path('menu/', views.menu, name='menu'),
    path('galeria/', galeria, name='galeria'),
    path('formulario/', formulario, name='formulario'),
    path('agregar_mascota/', views.agregar_mascota, name='agregar_mascota'),
    path('listar-mascotas/', listar_mascotas, name='listar_mascotas'),
    path('eliminar-mascota/<id>/', eliminar_mascotas, name='eliminar_mascota'),
    path('modificar-mascota/<id>/', modificar_mascota, name='modificar_mascota'),
    path('admin/', admin.site.urls),
]

"""