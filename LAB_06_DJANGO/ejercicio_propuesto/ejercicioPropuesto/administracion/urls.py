from django.urls import path
from .views import nuevo_alumno, nuevo_curso, nueva_nota, lista_alumnos, lista_cursos, lista_notas,eliminar_alumno, eliminar_curso, eliminar_nota

urlpatterns = [
    path('', nuevo_alumno, name='inicio'),
    path('nuevo_alumno/', nuevo_alumno, name='nuevo_alumno'),
    path('nuevo_curso/', nuevo_curso, name='nuevo_curso'),
    path('nueva_nota/', nueva_nota, name='nueva_nota'),
    path('lista_alumnos/', lista_alumnos, name='lista_alumnos'),
    path('lista_cursos/', lista_cursos, name='lista_cursos'),
    path('lista_notas/', lista_notas, name='lista_notas'),
    path('eliminar_alumno/<int:alumno_id>/', eliminar_alumno, name='eliminar_alumno'),
    path('eliminar_curso/<int:curso_id>/', eliminar_curso, name='eliminar_curso'),
    path('eliminar_nota/<int:nota_id>/', eliminar_nota, name='eliminar_nota'),

]   
    