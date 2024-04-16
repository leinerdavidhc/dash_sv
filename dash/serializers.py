from rest_framework import serializers
from .models import Vehiculo,Anotacion

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class AnotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anotacion
        fields = '__all__'

