from django.db import models

# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=1024)
    body = models.TextField()
    created_at = models.DateTimeField('date published')
    read = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    
    def __str__(self):
     return self.title
 