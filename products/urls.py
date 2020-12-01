from .views import delete_product, add_product, product_list, product_details, edit_product
from django.urls import path   
    
    
urlspattrens = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_details, name='product_details'),
    path('products/add/', add_product, name='add_product'),
    path('products/edit/<int:pk>/', edit_product, name='edit_product'),
    path('products/delete/<int:pk>', delete_product, name='delete_product'),
]