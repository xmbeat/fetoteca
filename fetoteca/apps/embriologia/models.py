from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Malformacion(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre

class Feto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	malformaciones = models.ManyToManyField('Malformacion')
	imagenes = models.ManyToManyField('ImagenFeto')

	def __unicode__(self):
		return self.nombre

class ImagenFeto(models.Model):
	url = models.CharField(max_length=1024)

	def __unicode__(self):
		return self.url