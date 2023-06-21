from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=15)
    contact = models.PositiveIntegerField()
    location = models.CharField( max_length= 25)
    store_name =models.CharField( max_length=32)
    password =models.PositiveIntegerField()
    user_name=models.CharField(max_length= 32)
    
    def __str__(self):
        return self.name
    
    
