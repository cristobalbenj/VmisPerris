"""misperris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
]

"""

from django.urls import path, include
from django.contrib import admin
from core.views import menu,home,agregar_mascotas,listar_mascotas,eliminar_mascotas,modificar_mascota,agregar_adoptante,listar_adoptantes,eliminar_adoptante,modificar_adoptante
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home,name='home'),
    path('menu/', views.menu,name='menu'),
    path('agregar_mascota/', views.agregar_mascotas, name='agregar_mascota'),
    path('listar-mascotas/', listar_mascotas, name='listar_mascotas'),
    path('eliminar-mascota/<id>/', eliminar_mascotas, name='eliminar_mascota'),
    path('modificar_mascota/<id>/', modificar_mascota, name='modificar_mascota'),
    path('agregar_adoptante/', agregar_adoptante, name='agregar_adoptante'),
    path('listar_adoptantes/', listar_adoptantes, name='listar_adoptantes'),
    path('eliminar-adoptante/<id>/', eliminar_adoptante, name='eliminar_adoptante'),
    path('modificar_adoptante/<id>/', modificar_adoptante, name='modificar_adoptante'),
]