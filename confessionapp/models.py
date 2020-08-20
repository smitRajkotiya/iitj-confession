from django.db import models
from django.utils import timezone


class conf(models.Model):
    email = models.EmailField(default="example@gmail.com")
    image = models.ImageField(upload_to='images/',null=True)
    desc = models.TextField(null=True)
    noofwows = models.IntegerField(null=True)
    noofangrey = models.IntegerField(null=True)
    noofhaha = models.IntegerField(null=True)
    currentdate= models.DateField(default=timezone.now)
