from rest_framework import serializers

from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
	"""
	A `ModelSerializer` for Dog model.

	Has the same fields as the Dog model and 3 extra fields:
		breed_average_age - for an average dogs age of the same breeds, calculates in a DogViewSet;
		breed_name - takes name of a breed from related table, just for convenience;
		dog_count - for counting a number of dogs of the same breeds, also calculates in a DogViewSet.
	"""
	breed_average_age = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2, coerce_to_string=False)
	breed_name = serializers.CharField(source='breed.name', read_only=True)
	dog_count = serializers.IntegerField(read_only=True)

	class Meta:
		model = Dog
		fields = [
			'id', 'name', 'age', 'gender', 'color',
			'favorite_food', 'favorite_toy', 'breed',
			'breed_name', 'dog_count', 'breed_average_age'
		]


class BreedSerializer(serializers.ModelSerializer):
	"""
	A `ModelSerializer` for Breed model.

	Has the same fields as the Breed model and 1 extra field:
		dog_count - for counting a number of dogs of the same breeds, also calculates in a BreedViewSet.
	"""
	dog_count = serializers.IntegerField(read_only=True)

	class Meta:
		model = Breed
		fields = [
			'id', 'name', 'size', 'friendliness',
			'trainability', 'shedding_amount',
			'exercise_needs', 'dog_count'
		]
