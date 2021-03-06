from django.db       import models


class User(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.CharField(max_length=100, unique=True)
    password   = models.CharField(max_length=200)
    contact    = models.CharField(max_length=100)
    address    = models.CharField(max_length=100)
    key        = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'users'

class Review(models.Model):
    user    = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        db_table = 'reviews'
