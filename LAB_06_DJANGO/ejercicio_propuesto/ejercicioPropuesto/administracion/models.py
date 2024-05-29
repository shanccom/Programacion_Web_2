from django.db import models

# Creacion de modelos propios

class Alumno(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    cui = models.CharField(max_length = 8, unique = True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

class NotasAlumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    nota = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f"{self.alumno} - {self.curso}: {self.nota}"