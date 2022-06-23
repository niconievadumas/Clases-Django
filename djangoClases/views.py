from django.http import HttpResponse
from datetime import datetime

from django.template import Context, Template

def inicio(request):
    return HttpResponse('Hola soy mi primer vista en Django')

def ver_fecha(request):
    return HttpResponse(f'Fecha actual: {datetime.now()}')

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}')
 
def mi_template(request):
    
    archivo = open(r'/Users/niconievadumas/Desktop/Programacion/CODER/Django clases/templates/prueba.html', 'r')
    
    template1 = Template(archivo.read())
    
    archivo.close()
    
    contexto1 = Context()
    
    render1 = template1.render(contexto1)
    
    return HttpResponse(render1)