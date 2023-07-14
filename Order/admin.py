from django.contrib import admin

# Register your models here.
from.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display=("order_name","order_name","order_total","date","delivery_date","cart","customer")
    
admin.site.register(Order,OrderAdmin)
    
