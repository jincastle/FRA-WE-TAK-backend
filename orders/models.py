from django.db       import models
from products.models import User
from products.models import Product


class Cart(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count   = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'carts'

class Order(models.Model):
    order_number = models.IntegerField()
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    address      = models.CharField(max_length=200)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_statuses'

class OrderItem(models.Model):
    order             = models.ForeignKey('Order', on_delete=models.CASCADE)
    count             = models.IntegerField()
    tracking_number   = models.CharField(max_length=200)
    product           = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_item_status = models.ForeignKey('OrderItemStatus', on_delete=models.CASCADE)
    address           = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'order_items'

class OrderItemStatus(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'order_item_statuses'
