from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Mascota,Raza,Genero,Estado,Adoptante,GeneroAdoptante,Region,Ciudad,tipoVivienda
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'core/home.html')

def home(request):
    return render(request, 'core/home.html')

def menu(request):
    return render(request, 'core/menu.html')



#AGREGAR OK
@login_required
def agregar_mascotas(request):

    razas = Raza.objects.all()
    generos = Genero.objects.all()
    estados = Estado.objects.all()
    variables = {
        'razas':razas,
        'generos':generos,
        'estados':estados
    }

    if request.POST:
        perro = Mascota()
        perro.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        perro.raza = raza
        genero = Genero()
        genero.id = request.POST.get('cboGenero')
        perro.genero = genero
        perro.imagen = request.POST.get('file_foto')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        perro.estado = estado

        try:
            perro.save()
            variables['mensaje'] = 'Mascota Guardada Correctamente'
        except:
            variables['mensaje'] = 'ERROR! No se ha podido guardar'

    return render(request, 'core/agregar_mascota.html', variables)
########################################################################



#LISTAR OK
def listar_mascotas(request):

    mascotas = Mascota.objects.all()

    return render(request,'core/listar_mascotas.html',{
        'mascotas':mascotas
    })
#############################################################

#ELIMINAR OK
def eliminar_mascotas(request, id):

    mascota = Mascota.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Mascota Eliminada Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar Mascota"
        messages.error(request, mensaje)
    
    return redirect('listar_mascotas')
#######################################################



def modificar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)
    razas = Raza.objects.all()
    generos = Genero.objects.all()
    estados = Estado.objects.all()
    variables = {
        'mascota':mascota,
        'razas':razas,
        'generos':generos,
        'estados':estados
    }

    if request.POST:
        perro = Mascota()
        perro.id = request.POST.get('txtId')
        perro.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        perro.raza = raza
        genero = Genero()
        genero.id = request.POST.get('cboGenero')
        perro.genero = genero
        perro.imagen = request.POST.get('file_foto')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        perro.estado = estado

        try:
            perro.save()
            messages.success(request, 'Mascota Modificada Exitosamente')
        except:
            messages.error(request, 'ERROR! No se ha podido modificar')
        return redirect('listar_mascotas')


    return render(request,'core/modificar_mascota.html', variables)


#AGREGAR OK
def agregar_adoptante(request):

    generos = GeneroAdoptante.objects.all()
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    viviendas = tipoVivienda.objects.all()
    mascotas = Mascota.objects.all()
    variables = {
        'generos':generos,
        'regiones':regiones,
        'ciudades':ciudades,
        'viviendas':viviendas,
        'mascotas':mascotas
    }

    if request.POST:
        adop = Adoptante()
        adop.nombre = request.POST.get('txtNombre')
        adop.rut = request.POST.get('txtRut')
        adop.email = request.POST.get('txtCorreo')
        adop.tel = request.POST.get('txtTelefono')
        adop.direccion = request.POST.get('txtDireccion')
        genero = GeneroAdoptante()
        genero.id = request.POST.get('cboGeneroAdoptante')
        adop.genero = genero
        region = Region()
        region.id = request.POST.get('cboRegion')
        adop.region = region #puede ser nombre adop.nombre = nombre
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        adop.ciudad = ciudad
        vivienda = tipoVivienda()
        vivienda.id = request.POST.get('cboVivienda')
        adop.vivienda = vivienda
        mascota = Mascota()
        mascota.id = request.POST.get('cboMascota')
        adop.mascota = mascota

        try:
            adop.save()
            variables['mensaje'] = 'Adoptante Guardado Exitosamente'
        except:
            variables['mensaje'] = 'ERROR! No se ha podido guardar'


    return render(request,'core/agregar_adoptante.html', variables)
########################################################################

#LISTAR OK
def listar_adoptantes(request):

    adop = Adoptante.objects.all()

    return render(request,'core/listar_adoptantes.html',{'adop':adop})
####################################################################

#ELIMINAR OK
def eliminar_adoptante(request, id):
    adop = Adoptante.objects.get(id=id)

    try:
        adop.delete()
        mensaje = "Adoptante Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "ERROR! No se ha podido Eliminar"
        messages.error(request, mensaje)
    
    return redirect('listar_adoptantes')
######################################################

def modificar_adoptante(request, id):

    adop = Adoptante.objects.get(id=id)
    generos = GeneroAdoptante.objects.all()
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    viviendas = tipoVivienda.objects.all()
    mascotas = Mascota.objects.all()
    variables = {
        'adop':adop,
        'generos':generos,
        'regiones':regiones,
        'ciudades':ciudades,
        'viviendas':viviendas,
        'mascotas':mascotas
    }

    if request.POST:
        ad= Adoptante()
        ad.id = request.POST.get('txtId')
        ad.nombre = request.POST.get('txtNombre')
        ad.rut = request.POST.get('txtRut')
        ad.email = request.POST.get('txtCorreo')
        ad.tel = request.POST.get('txtTelefono')
        ad.direccion = request.POST.get('txtDireccion')
        genero = GeneroAdoptante()
        genero.id = request.POST.get('cboGeneroAdoptante')
        ad.genero = genero
        region = Region()
        region.id = request.POST.get('cboRegion')
        ad.region = region
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        ad.ciudad = ciudad
        vivienda = tipoVivienda()
        vivienda.id = request.POST.get('cboVivienda')
        ad.vivienda = vivienda
        mascota = Mascota()
        mascota.id = request.POST.get('cboMascota')
        ad.mascota = mascota

        try:
            ad.save()
            messages.success(request, 'Adoptante Modificado Exitosamente')
        except:
            messages.error(request, 'ERROR! No se ha podido modificar')
        return redirect('listar_adoptantes')


    return render(request,'core/modificar_adoptante.html', variables)






