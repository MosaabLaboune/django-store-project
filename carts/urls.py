from .views import add_to_cart, cart, clear_cart, remove_from_cart
from django.urls import path   
    
    
urlpatterns = [

    path('', cart, name='cart'),
    path('cart/add/<product_id>', add_to_cart, name='add_to_cart'),
    path('cart/delete/<product_id>', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),



]
    