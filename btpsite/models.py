from django.db import models
from django.utils.html import mark_safe

# Create your models here.


STATUS_CHOICES = [
    ('DRAFT', 'Draft'),
    ('PUBLISHED', 'Published'),
    ('AUTRE', 'AUTRE'),
]

class Project(models.Model):
	image_link = models.ImageField(upload_to='btpsite_image', blank=True)
	title = models.CharField(max_length=250)
	description = models.TextField()
	categorie = models.ForeignKey('Categorie', on_delete= models.CASCADE)
	status = models.CharField(max_length=25, choices= STATUS_CHOICES,blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Project"
		verbose_name_plural = "Projects"

	def __str__(self):

		return self.title


	def image_tag(self):
		return mark_safe('<img src="/btpsite_image/%s" width="150" height="150" />' % (self.image_link))
    # image_tag.short_description = 'Image'

  


"""
Class Categorie 
"""

class Categorie(models.Model):
	name_categorie = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name_categorie

	class Meta:
		verbose_name = "Categorie"
		verbose_name_plural = "Categories"
"""

Client class 

"""

class Client(models.Model):

	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	telephone = models.CharField(max_length=255)


	def __str__(self):
		return f"{self.firstName}  {self.lastName}" 

	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Clients"


