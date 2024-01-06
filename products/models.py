from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Category") 

    

class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("SubCategory")
        verbose_name_plural = ("SubCategory") 

    
#checkbox
class Brand(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("CheckBox")
        verbose_name_plural = ("CheckBox")
    

class Color(models.Model):
    RED = '#b71c1c'
    GREEN = '#1b5e20'
    BLUE = '#303f9f'

    COLOR_CHOICES = [
        (RED, 'Red'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
    ]
    
    add_color = models.CharField(max_length=120)
    tag_color = models.CharField(max_length=7, choices=COLOR_CHOICES, default=RED)

    def __str__(self):
        return self.add_color

    

class Product(models.Model):

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='product_images/') 
    names_add = models.CharField(max_length=150)

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    content = HTMLField()
    rating =models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],default=5,verbose_name="Product Rating(max:5)"
    )

    price = models.DecimalField(max_digits=10, decimal_places=0)
    prices = models.DecimalField(max_digits=10, decimal_places=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Product") 


    def get_absolute_url(self):
        return reverse("products:shop-single", kwargs={"slug": self.slug})


    def image_add(self):
        return ProductImage.objects.filter(product_pro=self)
    
                 
class ProductImage(models.Model):
        product_pro = models.ForeignKey(Product, on_delete=models.CASCADE)
        image = models.ImageField()


# class ProductColor(models.Model):
#         product_pro = models.ForeignKey(Product, on_delete=models.CASCADE)
#         color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)




