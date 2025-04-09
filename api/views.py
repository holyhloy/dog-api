from django.db import models
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Dog
from api.serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        average_age_subquery = Dog.objects.filter(breed=models.OuterRef('breed')).values('breed').annotate(
            avg_age=models.Avg('age')).values('avg_age')
        queryset = Dog.objects.annotate(breed_average_age=models.Subquery(average_age_subquery))
        print(queryset)
        serializer = DogSerializer(instance=queryset, many=True)
        return Response(serializer.data)
