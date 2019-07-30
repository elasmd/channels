from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from api.package.models import Package


class Subscriptions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    date_subbed = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)