from django.shortcuts import render

from rest_framework import viewsets

from api.models import Dog
from api.serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
	queryset = Dog.objects.prefetch_related('dogs').all()
	serializer_class = DogSerializer