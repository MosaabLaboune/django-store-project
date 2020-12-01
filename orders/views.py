from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from products.models import Product
# Create your views here.
@login_required
def order(request):
    user = request.user
    products = user.cart.items.all()
    total_price = user.cart.total_price()
    return render(request, 'orders/order.html', {'products': products, 'total_price': total_price})