from django.db import models

# Create your models here.

class Shipment(models.Model):
    name = models.CharField(max_length=200)
    shipment_date = models.DateTimeField()
    shipment_status = models.CharField(max_length=200)
    shipment_type = models.CharField(max_length=200)
    
    
    def __str__(self) :
        return self.name
    
    
    
