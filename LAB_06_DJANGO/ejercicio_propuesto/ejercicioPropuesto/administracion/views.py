from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlumnoForm, CursoForm, NotasAlumnosPorCursoForm
from .models import Alumno, Curso, NotasAlumno

def nuevo_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'administracion/nuevo_alumno.html', {'form': form})

def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'administracion/nuevo_curso.html', {'form': form})

def nueva_nota(request):
    if request.method == "POST":
        form = NotasAlumnosPorCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotasAlumnosPorCursoForm()
    return render(request, 'administracion/nueva_nota.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'administracion/lista_alumnos.html', {'alumnos': alumnos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'administracion/lista_cursos.html', {'cursos': cursos})

def lista_notas(request):
    notas = NotasAlumno.objects.all()
    return render(request, 'administracion/lista_notas.html', {'notas': notas})

def eliminar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(pk=alumno_id)
    alumno.delete()
    return redirect('lista_alumnos')

def eliminar_curso(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    curso.delete()
    return redirect('lista_cursos')

def eliminar_nota(request, nota_id):
    nota = NotasAlumno.objects.get(pk=nota_id)
    nota.delete()
    return redirect('lista_notas')
