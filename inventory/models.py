from django.db import models
from  owner.models import Owner



# Create your models here.
class Products(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    name = models.CharField('Product Name', max_length=32)
    description =models.TextField('Description'  )
    image = models.ImageField('Image')
    price = models.DecimalField('Price',max_digits= 4, decimal_places= 4)
    stock = models.PositiveIntegerField('Stock')
    # Timestamp tells us when the object was created
    date_created= models.DateTimeField('Date',auto_now_add= True)
    date_updated = models.DateTimeField('Date updated',auto_now=2)
    
    
    # in  creating a model it is important to create a string represenation of that model
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
