from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contact')
