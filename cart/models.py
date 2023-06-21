from django.db import models

# Create your models here.
class Cart(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    payment_options = models.CharField(max_length= 32)
    date_updated= models.DateField( auto_now=False, auto_now_add=False)
    date_created =models.DateField( auto_now=False, auto_now_add=False)
    
    
    
    
    
    def __str__(self):
        return self.name
    
    
    