from django.urls import path
from .views import nuevo_alumno, nuevo_curso, nueva_nota, lista_alumnos, lista_cursos, lista_notas

urlpatterns = [
    path('', nuevo_alumno, name='inicio'),
    path('nuevo_alumno/', nuevo_alumno, name='nuevo_alumno'),
    path('nuevo_curso/', nuevo_curso, name='nuevo_curso'),
    path('nueva_nota/', nueva_nota, name='nueva_nota'),
    path('lista_alumnos/', lista_alumnos, name='lista_alumnos'),
    path('lista_cursos/', lista_cursos, name='lista_cursos'),
    path('lista_notas/', lista_notas, name='lista_notas'),
]   