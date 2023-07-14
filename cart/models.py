from django.db import models
from inventory.models import Products

# Create your models here.
class Cart(models.Model):
    inventory= models.ManyToManyField(Products)
    name = models.CharField(max_length=50)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    payment_options = models.CharField(max_length= 32)
    date_updated= models.DateField( auto_now=False, auto_now_add=False)
    date_created =models.DateField( auto_now=False, auto_now_add=False)
    delivery_choices= (
        ('1', 'Home Delivery'),
        ('2', 'Pick Up'),
        
    )
    
    
    
    
    
    def __str__(self):
        return f"Cart #{self.pk}"
    
    
    