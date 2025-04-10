from rest_framework import serializers

from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
	breed_average_age = serializers.FloatField(read_only=True)
	breed_name = serializers.CharField(source='breed.name', read_only=True)
	dog_count = serializers.IntegerField(read_only=True)

	class Meta:
		model = Dog
		fields = ['id', 'name', 'age', 'gender', 'color', 'favorite_food', 'favorite_toy', 'breed_name',
				  'dog_count', 'breed_average_age']


class BreedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Breed
		fields = '__all__'