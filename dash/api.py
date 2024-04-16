from rest_framework import viewsets,permissions
from .models import Vehiculo,Anotacion
from .serializers import VehiculoSerializer,AnotacionSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = VehiculoSerializer

class AnotacionViewSet(viewsets.ModelViewSet):
    queryset = Anotacion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = AnotacionSerializer