from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template, Context
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable

def inicio(request):
    return render(request, 'index.html')

def cursos(request):
    contexto = {
        'cursos' : {
            'desarrolloweb' : 'Desarrollo Web',
            'analisisdedatos' : 'Analisis de Datos',
            'diseñouxui' : 'Diseño UX/UI',
            
        }
    }
    return render(request, 'cursos.html', contexto)

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return redirect('AppCoderInicio')

def entregables(request):
    return render(request, 'entregables.html')

