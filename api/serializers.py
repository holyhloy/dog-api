from rest_framework import serializers

from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
	breed_average_age = serializers.FloatField(read_only=True)
	breed_name = serializers.CharField(source='breed.name')

	class Meta:
		model = Dog
		fields = ['id', 'name', 'age', 'gender', 'color', 'favorite_food', 'favorite_toy', 'breed_name', 'breed_average_age']
