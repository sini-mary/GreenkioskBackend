from django.db import models



# Create your models here.
class Vendor(models.Model):
    vendor_name= models.CharField('name' , max_length=64)
    location= models.CharField("location",max_length=50)
    contacts=models.IntegerField()
    store_name=models.CharField("Store Name",max_length=32)
    
    
    def __str__(self):
     return self.vendor_name
 