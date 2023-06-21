from django.contrib import admin
from.models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display =  ("name","price","quantity","payment_options","date_updated","date_created")
    
    
admin.site.register(Cart,CartAdmin)
