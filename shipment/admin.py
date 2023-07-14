from django.contrib import admin
from.models import Shipment

# Register your models here.

class ShipmentAdmin(admin.ModelAdmin):
    list_display=("name","shipment_date","shipment_status","shipment_type")
admin.site.register(Shipment,ShipmentAdmin)