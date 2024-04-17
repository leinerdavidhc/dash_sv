from rest_framework import viewsets,permissions
from .models import Vehiculo,Anotacion,Incidentes
from .serializers import VehiculoSerializer,AnotacionSerializer,IncidenteSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = VehiculoSerializer

class AnotacionViewSet(viewsets.ModelViewSet):
    queryset = Anotacion.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = AnotacionSerializer

class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incidentes.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = IncidenteSerializer