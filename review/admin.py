from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display= ("name","message","number_of_stars")
    
    def __str__(self):
        return self.name
admin.site.register(Review,ReviewAdmin)