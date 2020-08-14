from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

"""
    dispatch: valida la peticion y elige que metodo HTTP se utilizo para la solicitud
    http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
    options():
"""
# Create your views here.

class Inicio(TemplateView):
    #def get(self,request,*args,**kwargs):
    #    return render(request,'index.html')
    template_name = 'index.html'

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

    #def get(self,request,*args,**kwargs):
    #    autores = Autor.objects.filter(estado = True)
    #    return render(request,self.template_name,{'autores':autores})
#def home(request):
#    return render(request,'index.html')

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class EliminarAutor(DeleteView):
    model = Autor
    #success_url = reverse_lazy('libro:listar_autor')

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')

#def crearAutor(request):
#    if request.method == 'POST':
    #    nombre = request.POST.get('nombre')
    #    apellidos = request.POST.get('apellidos')
    #    nacionalidad = request.POST.get('descripcion')
    #    descripcion = request.POST.get('descripcion')
    #    autor = Autor(nombre = nombre, apellidos = apellidos, nacionalidad = nacionalidad, descripcion = descripcion)
    #    autor.save()
    #    return redirect('index')
    #return render(request, 'libro/crear_autor.html')
#        autor_form = AutorForm(request.POST)
#        if autor_form.is_valid():
#            autor_form.save()
#            return redirect('index')
#    else:
#        autor_form = AutorForm()

#    return render(request, 'libro/crear_autor.html',{'autor_form' : autor_form})

##def listarAutor(request):
#    autores = Autor.objects.filter(estado = True)
#    return render(request, 'libro/listar_autor.html',{'autores': autores})

#def editarAutor(request, id):
#    autor_form = None
#    error = None
#    try:
#        autor = Autor.objects.get(id = id)
#        if request.method == 'GET':
#            autor_form = AutorForm(instance = autor)
#        else:
#            autor_form = AutorForm(request.POST, instance = autor)
#            if autor_form.is_valid():
#                autor_form.save()
#            return redirect('libro:listar_autor')
#
#    except ObjectDoesNotExist as e:
#        error = e
#    return render(request,'libro/crear_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutor(request, id):
    autor = Autor.objects.get( id = id)
    if request.method == 'POST':
        #autor.delete()
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html',{'autor':autor})
