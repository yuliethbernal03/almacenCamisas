from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservices.views import *

router  = routers.DefaultRouter()
router.register(r'Categoria', fabric_viewset)
router.register(r'Pedido', shirt_viewset)
router.register(r'DatosProducto', product_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]