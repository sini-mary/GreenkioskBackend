
# Register your models here.
from django.contrib import admin
from.models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display =  ("name","contact","location","store_name","password","user_name",)
    
admin.site.register(Payment,PaymentAdmin)
