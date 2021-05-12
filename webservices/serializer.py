from rest_framework import serializers
from home.models import*

class fabric_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'Nombre', 'Descripcion')

class shirt_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ('url', 'Nombre', 'Fecha_Entrada', 'categoria', 'Cantidad')

class product_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DatosProducto
        fields = ('url', 'Nombre', 'Talla', 'Descripcion', 'categoria', 'pedido')

    