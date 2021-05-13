from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name = 'home_view'),
    path('about/', about_view, name = 'about_view'),
    path('contact/', contact_view, name = 'contact_view'),
    path('shirt_print/', shirt_print_view, name = 'shirt_print_view'),
    path('shirts/', shirts_view, name = 'shirts_view'),
    path('fabrics/', fabrics_view, name = 'fabrics_view'),
    path('add_shirt_print/', add_shirt_print_view, name = 'add_shirt_print_view'),
    path('add_tShirt/', add_tShirt_view, name = 'add_tShirt_view'),
    path('add_tFabric/', add_tFabric_view, name = 'add_tFabric_view'),
    path('see_shirt_print/<int:id_print>', see_shirt_print_view, name = 'see_shirt_print_view'),
    path('remove_shirt_print/<int:id_print>', remove_shirt_print_view, name = 'remove_shirt_print_view'),
    path('edit_shirt_print/<int:id_print>', edit_shirt_print_view, name = 'edit_shirt_print_view'),
    path('remove_tShirt/<int:id_shirt>', remove_tShirt_view, name = 'remove_tShirt_view'),
    path('edit_tShirt/<int:id_shirt>', edit_tShirt_view, name = 'edit_tShirt_view'),
    path('remove_tFabric/<int:id_fabric>', remove_tFabric_view, name = 'remove_tFabric_view'),
    path('edit_tFabric/<int:id_fabric>', edit_tFabric_view, name = 'edit_tFabric_view'),
]