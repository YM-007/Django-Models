from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=100)
    author = models.ForeignKey
    created_date = models.DateTimeField
    published_date = models.DateTimeField
    