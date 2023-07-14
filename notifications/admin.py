from django.contrib import admin
from.models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'body','created_at','read','user')
admin.site.register(Notification,NotificationAdmin)