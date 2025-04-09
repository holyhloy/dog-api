from rest_framework import serializers

from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dog
		fields = '__all__'

