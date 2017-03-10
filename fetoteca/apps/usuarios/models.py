from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
	matricula = models.CharField(max_length = 50, primary_key=True)
	nombre = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.EmailField()