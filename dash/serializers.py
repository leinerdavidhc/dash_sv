from rest_framework import serializers
from .models import Vehiculo,Anotacion,Incidentes

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class AnotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anotacion
        fields = '__all__'

class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentes
        fields = '__all__'

