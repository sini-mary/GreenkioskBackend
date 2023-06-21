from django.contrib import admin
from.models import Owner

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display =  ("name","contact","location","store_name","password","user_name",)
    
admin.site.register(Owner,OwnerAdmin)
