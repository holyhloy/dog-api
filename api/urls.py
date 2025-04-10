from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'dogs', views.DogViewSet)
router.register(r'breeds', views.BreedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
