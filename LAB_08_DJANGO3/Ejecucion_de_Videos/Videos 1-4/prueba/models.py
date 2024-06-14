from django.db import models

# Create your models here.

class Languaje(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
        
class FrameWork(models.Model):
    name = models.CharField(max_length = 10)
    languaje = models.ForeignKey(Languaje, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    name = models.CharField(max_length = 10)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name