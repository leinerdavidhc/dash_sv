from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import VehiculoViewSet,AnotacionViewSet

router = DefaultRouter()
router.register('api/vehiculos', VehiculoViewSet, 'vehiculos')
router.register('api/anotacion', AnotacionViewSet, 'anotacion')

urlpatterns=router.urls