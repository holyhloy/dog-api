from django.db import models
from django.db.models import CharField


class Breed(models.Model):
	"""Class for a Breed model.

	Used to Django ORM was able to bring data to the database

	Has no attributes.
	"""
	SIZE_CHOICES = [
		('tiny', 'Tiny'),
		('small', 'Small'),
		('medium', 'Medium'),
		('large', 'Large')
	]

	name = models.CharField(max_length=50)
	size = models.CharField(max_length=50, choices=SIZE_CHOICES)
	friendliness = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
	trainability = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
	shedding_amount = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
	exercise_needs = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

	def __str__(self) -> CharField:
		"""Tells Django what to return when model object calls

		Returns:
			A Django CharField 'name' for the model
		"""
		return self.name
