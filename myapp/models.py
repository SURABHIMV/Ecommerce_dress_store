from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class productt(models.Model):
     product = models.CharField(max_length=100,null=True)
     image = models.ImageField(upload_to="product_image/", null=True, blank=True)
     price= models.PositiveIntegerField(default=0)
     category= models.CharField(max_length=100,null=True)

class userr(models.Model):
     user_image = models.ImageField(upload_to="user_image/", null=True, blank=True)
     user_name = models.CharField(max_length=100,null=True)
     user_phone= models.CharField(max_length=100,null=True)


class CartItem(models.Model):
    product = models.ForeignKey(productt, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=0,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    user_name = models.CharField(max_length=100,null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.quantity} x {self.product}'

class wishlist(models.Model):
    product = models.ForeignKey(productt, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=0,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f'{self.quantity} x {self.product}'