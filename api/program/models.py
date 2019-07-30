from django.db import models

# Create your models here.
from api.package.models import Package


class Program(models.Model):
    name = models.CharField(max_length=100)
    package = models.ManyToManyField(Package)
    date_created = models.DateTimeField(auto_now_add=True)

