from .views import order
from django.urls import path   
    
    
urlpatterns = [

    path('order', order, name='order'),


]
    