from django.db import models
from products.models import Product
from accounts.models import User

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField()
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    price = models.FloatField()
    discount = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=255, choices=[('Requested', 'Requested'),('Dispatched', 'Dispatched'),('Delivered', 'Delivered'),('Cancelled', 'Cancelled'),], default='Requested')

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='reviews', null=True, blank=True)