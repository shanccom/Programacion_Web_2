from django import forms
from .models import Alumno, Curso, NotasAlumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'cui']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre']

class NotasAlumnosPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotasAlumno
        fields = ['alumno', 'curso', 'nota']