from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name = 'home_view'),
    path('about/', about_view, name = 'about_view'),
    path('contact/', contact_view, name = 'contact_view'),
    path('products/', products_view, name = 'products_view'),
    path('shirts/', shirts_view, name = 'shirts_view'),
    path('fabrics/', fabrics_view, name = 'fabrics_view'),
    path('add_product/', add_product_view, name = 'add_product_view'),
    path('add_tShirrt/', add_tShirt_view, name = 'add_tShirt_view'),
    path('add_tFabric/', add_tFabric_view, name = 'add_tFabric_view'),
]