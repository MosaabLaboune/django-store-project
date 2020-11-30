from .views import add_to_cart, cart, clear_cart, remove_from_cart
from django.urls import path   
    
    
urlpatterns = [

    path('', cart, name='cart'),
    path('add/<product_id>', add_to_cart, name='add_to_cart'),
    path('delete/<product_id>', remove_from_cart, name='remove_from_cart'),
    path('clear/', clear_cart, name='clear_cart'),



]
    