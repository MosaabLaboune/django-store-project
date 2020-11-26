from .views import products_list, product_details
from django.urls import path   
    
    
urlpatterns = [

    path('products/', products_list),
    path('products/<pk>', product_details, name='product_details'),

]
    