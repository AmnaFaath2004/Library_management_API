from django.db import models

# Create your models here.
class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Published_date = models.DateField()
    ISBN = models.CharField(unique=True, max_length=13)
    category = models.CharField(max_length=100)
    Is_available = models.BooleanField(default=True)