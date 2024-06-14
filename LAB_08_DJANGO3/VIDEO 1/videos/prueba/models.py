from django.db import models

# Create your models here.

class Languaje(models.Model):
    name = models.CharField(max_length = 10)

class FrameWork(models.Model):
    name = models.CharField(max_length = 10)
    languaje = models.ForeignKey(Languaje, on_delete = models.CASCADE)

    	