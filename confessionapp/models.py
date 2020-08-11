from django.db import models


class conf(models.Model):
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    nooflikes = models.IntegerField(default=0)
    noofloves = models.IntegerField(default=0)
    noofwows = models.IntegerField(default=0)
    noofsad = models.IntegerField(default=0)
    noofangrey = models.IntegerField(default=0)
    noofhaha = models.IntegerField(default=0)
