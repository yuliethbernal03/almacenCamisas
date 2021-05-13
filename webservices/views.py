from home.models import *
from .serializer import *
from rest_framework import viewsets
# Create your views here.
class fabric_viewset(viewsets.ModelViewSet):
    queryset = Tela.objects.all()
    serializer_class = fabric_serializer

class  shirt_viewset (viewsets.ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = shirt_serializer

class  product_viewset (viewsets.ModelViewSet):
    queryset = Estampados.objects.all()
    serializer_class = product_serializer