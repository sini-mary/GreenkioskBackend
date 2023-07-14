from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    name=models.CharField((""), max_length=50)
    location= models.CharField( max_length=50)
    email=models.EmailField((""), max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    
    
    
    def __str__(self) :
        return self.name    