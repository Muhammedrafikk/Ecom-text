from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Order(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address= models.TextField()
    pincode = models.CharField(max_length=100)


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Order")


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    Product = models.CharField(max_length=100)
    image=  models.ImageField(upload_to='media/product_image')
    qunatity= models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    price = models.IntegerField(default=False)

    def __str__(self):
        return f"{self.order} - {self.Product}"
    
    
    class Meta:
        verbose_name = ("OrderItem")
        verbose_name_plural = ("OrderItem")
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = 0  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Wishlist for {self.product.name}"

          
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)

