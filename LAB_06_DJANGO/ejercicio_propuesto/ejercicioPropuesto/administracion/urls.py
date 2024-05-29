from django.urls import path
from .views import nuevo_alumno, nuevo_curso, nueva_nota

urlpatterns = [
    path('nuevo_alumno/', nuevo_alumno, name='nuevo_alumno'),
    path('nuevo_curso/', nuevo_curso, name='nuevo_curso'),
    path('nueva_nota/', nueva_nota, name='nueva_nota'),
]