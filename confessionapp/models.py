from django.db import models


class conf(models.Model):
    email = models.EmailField(default="example@gmail.com")
    img = models.ImageField(upload_to='pics',null=True)
    desc = models.TextField(null=True)
    nooflikes = models.IntegerField(default=0)
    noofloves = models.IntegerField(default=0)
    noofwows = models.IntegerField(default=0)
    noofsad = models.IntegerField(default=0)
    noofangrey = models.IntegerField(default=0)
    noofhaha = models.IntegerField(default=0)
