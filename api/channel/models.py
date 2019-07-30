from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Channel(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
