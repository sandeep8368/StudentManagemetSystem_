from django.db import models

# Create your models here.
class studentModel(models.Model):
    name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 35)
    addr = models.CharField(max_length = 100)
    roll = models.IntegerField()
    