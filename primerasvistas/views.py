from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from django.template import Context, Template, loader

from primerasvistas.models import Perro

def inicio(request):
    return HttpResponse('Hola soy mi primer vista en Django')

def ver_fecha(request):
    return HttpResponse(f'Fecha actual: {datetime.now()}')

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}')

# v1
 
# def mi_template(request):
    
#     archivo = open(r'/Users/niconievadumas/Desktop/Programacion/CODER/Django clases/templates/prueba.html', 'r')
    
#     template1 = Template(archivo.read())
    
#     archivo.close()
    
#     nombre =  'la concha de su madre all boys'
    
#     contexto1 = Context({'nombre': nombre})
    
#     render1 = template1.render(contexto1)
    
#     return HttpResponse(render1)

# v2py
 
def mi_template(request, nombre_perro, edad_perro):
    
    # archivo = open(r'prueba.html', 'r')  
    
    template1 = loader.get_template('prueba.html')
    
    # template1 = Template(archivo.read()) 
    
    # archivo.close()
    
    # contexto1 = Context()

    nombre =  'la concha de su madre all boys version 2'
    apellido = 'rocanrolllll neneeeee'
    lista = [1,2,3,4,5,6,7]
    perro = Perro(nombre= nombre_perro, edad= edad_perro)
    perro.save()
      
    render1 = template1.render({'nombre': nombre, 'apellido': apellido, 'edad': 4400, "lista": lista, "perro": perro})
    
    return HttpResponse(render1)

def listado_perros(request):

    template = loader.get_template("listado_perros.html")

    lista_perros = Perro.objects.all()

    render = template.render({"lista": lista_perros})

    return HttpResponse(render)