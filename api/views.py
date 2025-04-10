from django.db import models
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import Dog, Breed
from api.serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        average_age_subquery = Dog.objects.filter(breed=models.OuterRef('breed')).values('breed').annotate(
            avg_age=models.Avg('age')).values('avg_age')
        queryset = Dog.objects.annotate(breed_average_age=models.Subquery(average_age_subquery))
        serializer = DogSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        dog_count_subquery = Dog.objects.filter(breed=models.OuterRef('breed')).values('breed').annotate(
            cnt=models.Count('id')).values('cnt')
        queryset = Dog.objects.annotate(dog_count=models.Subquery(dog_count_subquery))
        instance = queryset.get(id=kwargs.get('pk'))
        serializer = DogSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DogSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer