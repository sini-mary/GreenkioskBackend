from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display=("vendor_name","location","contacts","store_name")
    
admin.site.register(Vendor,VendorAdmin)