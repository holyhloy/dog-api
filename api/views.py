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
        queryset = Dog.objects.annotate(breed_average_age=models.Subquery(average_age_subquery)).order_by('id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(instance=queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        dog_count_subquery = Dog.objects.filter(breed=models.OuterRef('breed')).values('breed').annotate(
            cnt=models.Count('id')).values('cnt')
        queryset = Dog.objects.annotate(dog_count=models.Subquery(dog_count_subquery))
        try:
            instance = queryset.get(id=kwargs.get('pk'))
        except models.ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def list(self, request, *args, **kwargs):
        dog_count_subquery = Breed.objects.filter(id=models.OuterRef('id')).annotate(dogs=Dog.objects.filter(breed=models.OuterRef('breeds'))
                            .values('breed')).annotate(cnt=models.Count('id')).values('cnt')
        queryset = Breed.objects.annotate(dog_count=models.Subquery(dog_count_subquery))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(instance=page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(instance=queryset, many=True)
        return Response(serializer.data)
