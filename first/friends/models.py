from django.db import models

# Create your models here.
class country(models.Model):
    country = models.CharField(max_length=200)
    pincode = models.IntegerField(default=000000)

class user(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    country = models.ForeignKey(country, on_delete=models.SET_NULL, null=True)


