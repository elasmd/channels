from django.db import models

# Create your models here.
from api.channel.models import Channel


class Package(models.Model):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
