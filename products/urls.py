from .views import product_delete, product_edit, products_list, product_details, product_add
from django.urls import path   
    
    
urlpatterns = [

    path('products/', products_list, name='product_list'),
    path('products/add', product_add, name='product_add'),
    path('products/<pk>', product_details, name='product_details'),
    path('products/edit/<pk>', product_edit, name='product_edit'),
    path('products/delete/<pk>', product_delete, name='product_delete'),
    

]
    