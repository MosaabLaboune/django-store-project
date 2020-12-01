from django.db import models
from products.models import Product
from django.db.models.deletion import CASCADE

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, related_name='order', on_delete=CASCADE)
    items = models.ManyToManyField(Product)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total


    def __str__(self):
        return str(self.user)