from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template, Context
from AppCoder.models import Curso, Estudiantes, Profesor, Entregable
