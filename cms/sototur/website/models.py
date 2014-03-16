
from django.db import models
from tinymce import models as tinymce_models



class Category(models.Model):

	name = models.CharField(max_length=40)

	def __unicode__(self):

		return self.name

	class Meta:

		verbose_name = "Categoria"



class Package(models.Model):

	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="packages")
	category = models.ForeignKey("Category", null=True, blank=True)
	desc = tinymce_models.HTMLField()

	def __unicode__(self):

		return self.title

	class Meta:

		verbose_name = "Paquete"



class HomeBlock(models.Model):

	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="home_blocks")
	link = models.URLField(max_length=300, blank=True)
	category = models.ForeignKey(Category, blank=True, null=True)
	package = models.ForeignKey(Package, blank=True, null=True)

	def __unicode__(self):

		return self.name

	class Meta:

		verbose_name = "Bloque Inicio"
		verbose_name_plural = "Bloques Inicio"


class HomeSlide(models.Model):

	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="home_blocks")
	link = models.URLField(max_length=300, blank=True)
	category = models.ForeignKey(Category, blank=True, null=True)
	package = models.ForeignKey(Package, blank=True, null=True)

	def __unicode__(self):

		return self.name

	class Meta:

		verbose_name = "Imagen Carrusel"
		verbose_name_plural = "Imagenes Carrusel"

