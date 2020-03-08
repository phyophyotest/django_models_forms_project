from django.db import models
import datetime
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    image=models.ImageField()
    create_at=models.DateTimeField(auto_now_add=True)
