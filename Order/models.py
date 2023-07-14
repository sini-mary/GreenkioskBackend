from django.db import models
from customer.models import Customer
from cart.models import Cart
from shipment.models import Shipment

# Create your models here.
class Order(models.Model):
    order_name=models.CharField("Name", max_length=50)
    order_number=models.IntegerField('Order number')
    order_total=models.FloatField("Order Total" )
    date=models.DateField(("Date"), auto_now=False, auto_now_add=False)
    delivery_date=models.DateTimeField((""), auto_now=False, auto_now_add=False)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"Order #{self.pk}"
    