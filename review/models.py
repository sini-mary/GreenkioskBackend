from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length= 72)
    number_of_stars = models.PositiveIntegerField()
    