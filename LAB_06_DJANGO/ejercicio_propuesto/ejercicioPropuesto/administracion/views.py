from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotasAlumnosPorCursoForm

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
