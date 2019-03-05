from django.db import models

# Create your models here.


class Stuff(models.Model):
	name = models.CharField('Название', max_length=100)


class Categories(models.Model):
	type = models.IntegerField('Тип категории')
	name = models.CharField('Название категории', max_length=100)
	parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.name