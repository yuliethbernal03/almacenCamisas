from rest_framework import serializers
from home.models import*

class fabric_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tela
        fields = ('url', 'Nombre', 'Descripcion')

class shirt_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Camisa
        fields = ('url', 'Nombre', 'Fecha_Entrada', 'categoria', 'Cantidad')

class product_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estampados
        fields = ('url', 'Nombre', 'Talla', 'Descripcion', 'categoria', 'pedido')

    