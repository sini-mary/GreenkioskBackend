from django.db import models
from customer.models import Customer
from cart.models import Cart
from shipment.models import Shipment

# Create your models here.
class Order(models.Model):
    order_number=models.IntegerField('Order number', max_length= 32)
    order_total=models.FloatField("Order Total",max_length=32 )
    date=models.DateField(("Date"), auto_now=False, auto_now_add=False)
    delivery_date=models.DateTimeField((""), auto_now=False, auto_now_add=False)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    shipments = models.ManyToManyField(Shipment, blank=True)