from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

